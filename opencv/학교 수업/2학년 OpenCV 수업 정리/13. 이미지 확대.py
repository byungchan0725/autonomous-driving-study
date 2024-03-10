import cv2 

src = cv2.imread('/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/img.png', cv2.IMREAD_COLOR)
h, w, c = src.shape 

dst1 = cv2.pyrUp(src, dstsize=(w*2, h*2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()