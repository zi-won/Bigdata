import cv2
# 비디오 캡처 객체 생성
cap = cv2.VideoCapture('data/opencv_data/video.avi')

frame_width = int(cap.get(3)) # 입력 동영상 프레임 크기, FPS 가져오기
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# 동영상 저장을 위한 비디오 객체 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 설정 (XVID)
out = cv2.VideoWriter('data/opencv_data/save_video.avi',fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame) # 영상 저장
    cv2.waitKey(int(1000/fps))
    cv2.imshow('Video', frame) # 비디오 프레임 출력
    if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' 키를 누르면 종료
        break
cap.release()
cv2.destroyAllWindows()