import cv2

src = cv2.imread("/Users/kimbyungchan/Desktop/Study/Computer Vision/OpenCV/학교 OpenCV/data/coffee.jpg")
src = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
dst = src.copy()

# 사용되는 예시 
# - 자율 주행: 도로에서의 코너를 검출 -> 차선 유지 및 회전 
# - 로봇 네비게이션: 환경의 구석구석을 돌아다니며 코너를 검출 

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
# ... (이미지, 코너 최댓값, 코너 품질, 최소 거ㅣㄹ, 마크스, 블록 크기, 해리스 코너 검출기, 핼리스 코너 계수)
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)

for i in corners:
    x, y = i.ravel()
    center = (int(x), int(y))
    cv2.circle(dst, center, 3, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()