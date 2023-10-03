import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame) # 비디오 프레임 출력
    if cv2.waitKey(1) & 0xFF == ord('q'): # q키를 누르면 종료
        break
    
cap.release()
cv2.destroyAllWindows(); 
