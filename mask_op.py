import cv2

src=cv2.imread('airplane.bmp',cv2.IMREAD_COLOR)
mask=cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst=cv2.imread('field.bmp', cv2.IMREAD_COLOR)
cv2.copyTo(src,mask,dst)
cv2.imshow("dst",dst)
cv2.imwrite("dst.bmp",dst)
cv2.waitKey()
cv2.destroyAllWindows()