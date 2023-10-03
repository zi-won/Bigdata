import numpy as np
import cv2

def onMouse(event, x, y, flag, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        print('마우스 왼쪽 버튼 누르기')
    elif event == cv2.EVENT_RBUTTONDOWN :
        print('마우스 오른쪽 버튼 누르기')
    elif event == cv2.EVENT_LBUTTONUP :
        print('마우스 왼쪽 버튼 떼기')
    elif event == cv2.EVENT_RBUTTONUP :
        print('마우스 오른쪽 버튼 떼기')
    print('마우스 이벤트 발생 x : ', x, 'y : ', y)
img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255

cv2.imshow('mouse Event1', img)
cv2.imshow('mouse Event2', img)
cv2.setMouseCallback('mouse Event1', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
