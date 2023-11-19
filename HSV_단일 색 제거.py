import cv2
src = cv2.imread('./data/tomato.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
lower_orange = (8*2, 50, 50)
upper_orange = (20*2, 255, 255)
mask = cv2.inRange(hsv, lower_orange, upper_orange)
not_mask = cv2.bitwise_not(mask)
orange = cv2.bitwise_and(src, src, mask = not_mask)
cv2.imshow('orange', orange)
cv2.waitKey()
cv2.destroyAllWindows()