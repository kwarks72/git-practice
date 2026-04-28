import matplotlib.pyplot as plt
import cv2

# 컬러 이미지
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.imshow(imgRGB)

# 흑백 이미지
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.subplot(122)
plt.axis('off')
plt.imshow(imgGray, cmap='gray')

plt.show()