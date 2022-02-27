import cv2

# img = cv2.imread('pic2.jpeg')
# cv2.imshow('Friends',img)
# cv2.waitKey(0)

frameWidth = 640
frameHeight = 320

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    success,img = cap.read()
    cv2.imshow('LiveCam',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break