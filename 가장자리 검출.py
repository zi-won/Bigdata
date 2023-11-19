import cv2
# 가장자리는 픽셀의 밝기가 급격하게 변하는 부분
# 예시) 로봇 가장 자리 검출을 사용하여 장애물 감지 및 회피
# 의료에서 X-ray 또는 MRI 스캔이미에서 해부학적 구조의 경계를 찾는데 사용
# 제조업에서  제품의 가장 자리를 검출하여 결함을 감지하거나 제품의 치수를 측정하는데 활용
src = cv2.imread('./data/tomato.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 소벨 함수(cv2.Sobel)로 입력 이미지에서 가장 자리를 검출
# sv2.Sobel(src(입력이미지), ddepth(출력 이미지 정밀도), dx(x 방향 미분 차수), dy(y 방향 미분 차수), ksize(커널 크기), delta(), borderType)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize = 3)
canny = cv2.Canny(src, 100, 255)
cv2.imshow('sobel', sobel)
cv2.imshow('laplacian', laplacian)
cv2.imshow('canny', canny)
cv2.waitKey()
cv2.destroyAllWindows()
