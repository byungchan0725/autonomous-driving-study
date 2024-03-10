import cv2
import numpy as np

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8) + 255  # 3x512x512 형태의 이미지 생성
x1, x2 = 100, 400
y1, y2 = 100, 400

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()