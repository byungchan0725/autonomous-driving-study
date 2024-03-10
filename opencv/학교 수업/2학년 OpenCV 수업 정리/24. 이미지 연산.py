import cv2 
import numpy as np 

src = cv2.imread('/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/fox.png')
number1 = np.ones_like(src) * 127 
number2 = np.ones_like(src) * 2

# 여러 이미지 겹치기 -> 고해상도 
add = cv2.add(src, number1)

# 배경 제거 -> 움직임 감지 
sub = cv2.subtract(src, number1)

# 명함 조절, 색상채도 조절
mul = cv2.multiply(src, number2)

# 노이즈 제거 
div = cv2.divide(src, number2)

src = np.concatenate((src, src, src, src), axis=1)
number = np.concatenate((number1, number1, number2, number2),axis=1)
dst = np.concatenate((add, add, mul, div), axis=1)
result = np.concatenate((src, number, dst), axis=0)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()