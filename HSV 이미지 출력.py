import cv2
src = cv2.imread('./DATA/tomato.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BAYER_BG2BGR)
h, s, v = cv2.split(hsv)

cv2.imshow('h', h) # 색상(Hue)
cv2.imshow('s', s) # 채도(Saturation)
cv2.imshow('v', v) # 명도(Value)
cv2.waitKey()
cv2.destroyAllWindows()