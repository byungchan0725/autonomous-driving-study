import numpy as np 
import cv2 

image = np.zeros((200, 400), np.uint8)
image.fill(255)  # 흰색으로 

title1, title2 = 'Autosize', 'Normal'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 600, 600)
cv2.resizeWindow(title2, 600, 600)

cv2.waitKey(0)
cv2.destroyAllWindows()