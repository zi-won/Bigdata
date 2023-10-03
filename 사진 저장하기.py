import cv2
image = cv2.imread('data/opencv_data/img.png')

cv2.imshow('Image', image)
key = cv2.waitKey(0)
if key == ord('s'): # 's' 키를 누르면 이미지 저장
    cv2.imwrite('data/opencv_data/save_img.png', image)
    print('Image saved successfully!')
cv2.destroyAllWindows()