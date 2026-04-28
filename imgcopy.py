import cv2

img1=cv2.imread('HappyFish.jpg')
img2=img1
img3=img1.copy()
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow()
cv2.waitKey()