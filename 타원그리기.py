import cv2
import numpy as np

img = np.zeros(shape=(512, 512, 3), dtype = np.uint8) + 255
ptCenter = img.shape[0] // 2, img.shape[1] // 2
size = 200, 100
cv2.ellipse(img, ptCenter, size, 0, 0, 360, (255, 0, 0))   # 1. 큰 파랑
cv2.ellipse(img, ptCenter, size, 45, 0, 360, (0, 0, 255))  # 2. 큰 빨강

box = (ptCenter, size, 0)
cv2.ellipse(img, box, (255, 0, 0))                         #3. 작은 파랑
box = (ptCenter, size, 45)
cv2.ellipse(img, box, (255, 0, 255), 5)                    #4. 작은 빨강
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()