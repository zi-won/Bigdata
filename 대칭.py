import cv2
src = cv2.imread('./data/img.png', cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)
# flipCode < 0는 xy 축 대칭(상하좌우 대칭)을 적용합니다
# flipCode = 0는 xy축 대칭(상화 대칭)을 적용합니다
# flipCode > =는 xy축 대칭(좌우 대칭)을 적용합니다
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()