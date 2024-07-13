import cv2
import numpy as np

img = cv2.imread('char_1.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print (M)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(img, [approx], 0, (0,255,0), 3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()