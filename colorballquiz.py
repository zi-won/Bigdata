import cv2
import numpy as np

src = cv2.imread('./data/colorball.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

lower_orange = (5, 70, 70)  # 오렌지 색상 범위
upper_orange = (20, 190, 190)

mask = cv2.inRange(hsv, lower_orange, upper_orange)

result = cv2.bitwise_and(src, src, mask=mask)

gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=10, minRadius=80, maxRadius=120)
orange = cv2.bitwise_and(src, src, mask=mask)

# Create a black mask
mask_black = np.zeros_like(src, dtype=np.uint8)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]

        # Draw circle and center on the black mask
        cv2.circle(mask_black, center, radius, (255, 255, 255), 5)
        cv2.circle(mask_black, center, 5, (255, 255, 255), -1)

# Bitwise-and the black mask with the original image
result_final = cv2.bitwise_and(src, mask_black)

cv2.imshow('Orange Color and Circles', result_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
