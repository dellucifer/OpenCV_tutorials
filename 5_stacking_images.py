import cv2
import numpy as np


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
    # cv2.imshow('LiveCam',img)

    kernel = np.ones((5,5),np.uint8)
    # img = cv2.imread('pic2.jpeg')
    img = cv2.resize(img,(400,230))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #grayscale image
    img_blur = cv2.GaussianBlur(img,(5,5),0)  #blur image
    img_canny = cv2.Canny(img, 200,200)     #will highlight the edges
    img_dilation = cv2.dilate(img_canny,kernel,iterations=1)
    img_erode = cv2.erode(img_dilation,kernel,iterations=1)

    # img1 = cv2.resize(img,(0,0),None,0.5,0.5)

    # Changing from 1 channel to 3 channel so that np don't throw error
    img_gray = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)
    img_canny = cv2.cvtColor(img_canny,cv2.COLOR_GRAY2BGR)
    img_dilation = cv2.cvtColor(img_dilation,cv2.COLOR_GRAY2BGR)
    img_erode = cv2.cvtColor(img_erode,cv2.COLOR_GRAY2BGR)
    img_bgr = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    img_HLS = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
    img_LAB = cv2.cvtColor(img,cv2.COLOR_RGB2LAB)
    img_HSV = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

    hor_stacked1 = np.hstack((img,img_gray,img_blur))   #img_canny,img_dilation,img_erode
    hor_stacked2 = np.hstack((img_canny,img_dilation,img_HSV))
    hor_stacked3 = np.hstack((img_bgr,img_HLS,img_erode))
    ver_stacked = np.vstack((hor_stacked1,hor_stacked2,hor_stacked3))

    # cv2.imshow('Image', img)
    # cv2.imshow('Gray_Image', img_gray)
    # cv2.imshow('Blur_Image',img_blur)
    # cv2.imshow('Canny_Image', img_canny)
    # cv2.imshow('Dilated_Image', img_dilation)
    # cv2.imshow('Eroded_Image', img_erode)
    # cv2.imshow('Horizontally Stacked1',hor_stacked1)
    # cv2.imshow('Horizontally Stacked2',hor_stacked1)
    cv2.imshow('Horizontally Stacked2', ver_stacked)
    # cv2.waitKey(0)
    # cv2.imshow('img1',img1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break