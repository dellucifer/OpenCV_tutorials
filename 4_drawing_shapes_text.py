import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)   #by dfault, np.zeroes will create image having float values, so make it int
print(img.shape)
#img[:] = 255,0,0   #will change the values of blue channel to 255

cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),thickness=2)
cv2.line(img,(0,img.shape[1]),(img.shape[0],0),(0,0,255),thickness=2)
cv2.line(img,(0,256),(512,256),(255,0,0),thickness=2)

cv2.rectangle(img,(12,12),(500,500),(0,255,255),thickness=2)
cv2.rectangle(img,(92,92),(420,420),(255,0,255),thickness=2)
cv2.rectangle(img,(172,172),(340,340),(255,255,0),cv2.FILLED)

cv2.circle(img,(256,256),244,(255,255,255),thickness=2)
cv2.circle(img,(256,256),164,(128,128,128),thickness=2)
cv2.circle(img,(256,256),84,(90,100,100),cv2.FILLED)

cv2.putText(img,'Hi,There!',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),thickness=1)

cv2.imshow('blank_image',img)
cv2.waitKey(0)