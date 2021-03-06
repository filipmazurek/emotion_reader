import cv2

# Mac Dependencies
# pip install numpy
# pip install opencv-python
#  on python 3 systems

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('captured_image.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
