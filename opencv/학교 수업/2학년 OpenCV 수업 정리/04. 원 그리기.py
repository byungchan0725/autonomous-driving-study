import cv2
import numpy as np

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8) + 255  # 3x512x512 형태의 이미지 생성
cx = img.shape[0] // 2  # 512 // 2
cy = img.shape[1] // 2  # 512 // 2

# 순서: 캔버스, 첫지점, 반지름, 색(B G R) 순서
cv2.circle(img, (cx, cy), 100, (0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()