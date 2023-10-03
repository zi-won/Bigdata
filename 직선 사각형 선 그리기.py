import cv2
import numpy as np
# 휜색 배경 생성
img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255
# 다른 색 예시
# img = np.full((512, 512, 3), (255, 0, 0), dtype = np.uint8) # bgr임, rgb랑 순서 다름

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 10) # 맨 마지막 칸을 10으로 바꾸면 굵기 바뀜

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 10)
cv2.line(img, (0, 0), (0, 500), (0, 0, 255), 10)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()