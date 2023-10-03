import cv2
cap = cv2.VideoCapture('data/opencv_data/video.avi')
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame) # 비디오 프레임 출력
    if cv2.waitKey(1) & 0xFF == ord('q'): # q키를 누르면 종료
        break
    if cv2.waitKey(1) & 0xFF == ord('s'): # s키를 누르면 저장
        count = count + 1
        cv2.imwrite('data/opencv-data/save_img'+str(count)+'.png', frame)
        print('Image saved successfully!')
            
cap.release()
cv2.destroyAllWindows(); 
