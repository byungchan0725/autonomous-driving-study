import cv2 

# 가장자리는 픽셀의 밝기가 급격하게 변함 
src = cv2.imread('/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/fox.png', cv2.IMREAD_COLOR)

# 1. 입력 이미지(src) 
# 2. 정밀(deepth) 
# 3. 방향 미분 차수(ksize)
gray = src
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(src, 100, 255)

cv2.imshow('src', src)
cv2.imshow('sobel', sobel)
cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()