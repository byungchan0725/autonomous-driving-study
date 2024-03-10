import cv2

image = cv2.imread('./data/img.png')

# 순서: image, text, 첫시점, 폰트, 폰트 크기, 글 색깔, 글 굵기
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('image_rgb', image_rgb)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()