import cv2
from ultralytics import YOLO
cap = cv2.VideoCapture('rtsp://210.99.70.120:1935/live/cctv001.stream')
model = YOLO('./yolov8_pretrained/yolov8n.pt')

while True:
    ret, frame = cap.read()
    result = model.predict(frame, save=False, conf=0.3)
    if not ret:
        break
    cv2.imshow('yolo', result[0].plot())
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
