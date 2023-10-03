import cv2
image = cv2.imread('data/opencv_data/img.png')
# 특정 시간동안 이미지 보여주기
cv2.imshow('Timed Display', image)
cv2.waitKey(3000) # 3초 동안 이미지 출력

# BGR 색 공간을 RGB로 변경
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', image_rgb)
cv2.waitKey(0)

# 흑백 이미지 출력
gray_rgb = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
cv2.imshow('Gray', gray_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
