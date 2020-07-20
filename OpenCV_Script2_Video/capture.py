import cv2
import time

video = cv2.VideoCapture(0)
a = 1

while True:
    a += 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # time.sleep(3)
    cv2.imshow('Capturing', gray)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()