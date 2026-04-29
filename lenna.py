import cv2
import numpy as np

# 이미지 불러오기 (컬러)
src = cv2.imread('lenna.bmp')

# 예외 처리 (파일 없을 때)
if src is None:
    print("이미지 불러오기 실패")
    exit()

# 방법 1: OpenCV (자동 saturate)
dst1 = cv2.add(src, (100, 100, 100))

# 방법 2: numpy (수동 saturate)
dst2 = np.clip(src + 100, 0, 255).astype(np.uint8)

# 결과 출력
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()