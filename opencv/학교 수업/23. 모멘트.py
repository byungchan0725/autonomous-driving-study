import cv2 

src = cv2.imread('/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/convex.png')
dst = src.copy() 
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours:
    M = cv2.moments(i)
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])

    cv2.circle(dst, (cX,cY), 3, (255, 0, 0), -1)
    cv2.drawContours(dst, [i], 0, (0, 0, 255), 2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()