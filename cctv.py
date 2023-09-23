import cv2
cap = cv2.VideoCapture('rtsp://210.99.70.120:1935/live/cctv001.stream')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()
