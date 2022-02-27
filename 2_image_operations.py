import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
img = cv2.imread('pic2.jpeg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #grayscale image
img_blur = cv2.GaussianBlur(img,(5,5),0)  #blur image
img_canny = cv2.Canny(img, 200,200)     #will highlight the edges
img_dilation = cv2.dilate(img_canny,kernel,iterations=1)
img_erode = cv2.erode(img_dilation,kernel,iterations=3)

# cv2.imshow('Image', img)
# cv2.imshow('Gray_Image', img_gray)
# cv2.imshow('Blur_Image',img_blur)
cv2.imshow('Canny_Image', img_canny)
cv2.imshow('Dilated_Image', img_dilation)
cv2.imshow('Eroded_Image', img_erode)
cv2.waitKey(0)