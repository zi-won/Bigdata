import cv2
import numpy as np

src = cv2.imread('./data/colorball.jpg')
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=10,minRadius=80, maxRadius=120)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        center = (i[0], i[1])
        radius=i[2]
        cv2.circle(dst, center, radius, (255,255,255),5)
        
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
