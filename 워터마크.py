import cv2
image = cv2.imread('data/opencv_data/img.png')
text = 'OpenCV Programming'
org = (50, 100)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text, org, font, 1, (0, 0, 255), 2)                        # 글자
cv2.imshow('img', image)
cv2.waitKey()
cv2.destroyAllWindows()