import cv2
src = cv2.imread('./data/img.png', cv2.IMREAD_COLOR)
# 높이, 너비, 채널 값을 저장하여 회전할 중심점을 설정

height, width, channel = src.shape
# 중심점, 각도, 비율로 매핑 변환행렬(matrix),
#                                (center, angle, scale)
print(height)
print(width)
print(channel)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 80, 1)
# 원본이미지(src)에 M(아핀 맵 행렬)을 적용하고 출력 이미지 크기(dsize)로 변경
# 출력 이미지(dst)를 반환합니다
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()