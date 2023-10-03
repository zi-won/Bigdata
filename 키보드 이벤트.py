import numpy as np
import cv2
img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255

switch_case = {
    ord('a') : 'a키 입력',
    ord('b') : 'b키 입력',
    0x41 : 'A키 입력',
    int('0x42', 16) : 'B키 입력'
}
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event', img)
while True :
    key = cv2.waitKey(100) # 0.1초 이벤트 대기
    if key == 27: # esc
        break
    try :
        result = switch_case[key]
        print(result)
    except KeyError :
        result = -1
cv2.destroyAllWindows()
    