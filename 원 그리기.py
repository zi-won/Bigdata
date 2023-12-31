import cv2
import numpy as np
# 휜색 배경 생성
img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255
cx = img.shape[0]//2
cy = img.shape[1]//2

for r in range(200,0,-100):
    cv2.circle(img, (cx, cy), r,color = (255, 0, 0))
        #  캔버스 시작점   반지름     색깔                 선 굵기
cv2.circle(img, (cx, cy), radius=5 ,color = (0, 0, 255), thickness=-1)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()