import cv2 

src = cv2.imread('/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/img.png', cv2.IMREAD_COLOR)
h, w, c = src.shape

matrix = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)  # 중심점, 각도, 비율 
dst = cv2.warpAffine(src, matrix, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()