import cv2
# 예시) 지형 모델링 : 지형의 높이 점들을 사용하여 지형의 경계를 근사화 하는데 사용
# 물체 검출 : 블록 껍질은 물체 주변의 경계를 찾고 물체를 식별하는데 사용

src = cv2.imread('./data/convex.png')
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours :
    hull = cv2.convexHull(i, clockwise=True)
    cv2.drawContours(dst, [hull], 0, (0,0,255), 2)
    
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()