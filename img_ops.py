import cv2
import numpy as np

# 비어있는 이미지 (값 랜덤 느낌)
img1 = np.empty((480, 640), dtype=np.uint8)

# 검정색 이미지
img2 = np.zeros((480, 640, 3), dtype=np.uint8)

# 흰색 이미지
img3 = np.ones((480, 640), dtype=np.uint8) * 255

# 노란색 이미지 (BGR: 255,255,0)
img4 = np.full((480, 640, 3), (255, 255, 0), dtype=np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()