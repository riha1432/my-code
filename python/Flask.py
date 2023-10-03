from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import time

camera = cv2.VideoCapture('rtsp://210.99.70.120:1935/live/cctv001.stream')
model = YOLO('./yolov8_pretrained/yolov8n.pt')
app = Flask(__name__)

def gen_frames():
  ret, frame = 0,0
  while True:
    for i in range(3):
        ret, frame = camera.read()
    if not ret:
      break
    else:
      result = model.predict(frame, save=False, conf=0.4)
      ret, buffer = cv2.imencode('.jpg', result[0].plot())
      frame = buffer.tobytes()
      yield (b'--frame\r\n'
                     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
  return render_template('video.html')

if __name__ == "__main__":
  app.run(debug=True)