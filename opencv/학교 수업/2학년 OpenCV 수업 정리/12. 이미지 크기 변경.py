import cv2 

src = cv2.imread('/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/img.png', cv2.IMREAD_COLOR)

 # 방법 1, 절대 크기로 변경 
dst1 = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_LINEAR)

# 방법 2, 비율에 맞게 상대 크기로 변경 (보간법)
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()