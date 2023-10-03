import cv2
# import numpy as np
image = cv2.imread('data/opencv_data/tiger.jpg')

pt1 = 100, 100
pt2 = 400, 400

# 캔버스, 시작점, 끝점 (B, G, R), 선 굵기
cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)
cv2.line(image, (150, 100), (150, 400), (0,0,255), 5)
cv2.line(image, (200, 100), (200,400), (0, 0, 255), 10)

cv2.imshow('img', image)
cv2.waitKey()
cv2.destroyAllWindows()