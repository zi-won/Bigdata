import cv2
src = cv2.imread('./DATA/tomato.jpg', cv2.IMREAD_COLOR)
height, width, channel = src.shape

print(height)
print(width)
print('BGR B', src[100, 100, 0])
print('BGR G', src[100, 100, 1])
print('BGR R', src[100, 100, 2])

src[100:120, 100, 120] = (255, 255, 0)
cv2.imshow('update image', src)
cv2.waitKey()
cv2.destroyAllWindows()

