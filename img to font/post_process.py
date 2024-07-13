import cv2

img = cv2.imread('a.png',cv2.IMREAD_REDUCED_GRAYSCALE_2)
cv2.imwrite('a2.png', img)