import cv2 

path = '../data/elon musk.mp4'
cap = cv2.VideoCapture(path)

while cap.isOpened():
    ret, frame = cap.read() 

    if ret:
        cv2.imshow('elon musk', frame)
        if cv2.waitKey(1) == ord('q'):
            break 
    else:
        break 

cv2.destroyAllWindows()
cap.release()