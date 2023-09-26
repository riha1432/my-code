from flask import Flask, render_template, Response
import cv2
html = "<!DOCTYPE html><html>\
   <head>\
    <title>Video Streaming</title>\
  </head>\
  <body>\
    <h1>Video Streaming</h1>\
    <img src=""{{ url_for('video_feed') }}"" width=""640"" height=""480"" />\
  </body>\
</html>\
"
camera = cv2.VideoCapture('rtsp://210.99.70.120:1935/live/cctv001.stream')
app = Flask(__name__)

def gen_frames():
  while True:
    success, frame = camera.read()  # read the camera frame
    if not success:
      break
    else:
      ret, buffer = cv2.imencode('.jpg', frame)
      frame = buffer.tobytes()
      yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
  return html

if __name__ == "__main__":
  app.run()