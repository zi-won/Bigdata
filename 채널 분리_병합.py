import cv2
import numpy as np

src = cv2.imread('./DATA/tomato.jpg', cv2.IMREAD_COLOR)
b, g, r = cv2.split(src)
# 분리된 채널들은 단일 채널이므로 흑백 세상으로 표현
inverse = cv2.merge((r,g,b))
# 채널 병합 함수는 분리된 채널을 병합해 하나의 이미지로 합칠 수 있음

# 빈 이미지 생성
height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype = np.uint8)
bgz = cv2.merge((b, g, zero))

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.imshow('inverse', inverse)
cv2.waitKey()
cv2.destroyAllWindows()
