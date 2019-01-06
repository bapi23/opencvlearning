import numpy as np
import cv2

img = cv2.imread("players.jpg",1)

#skalowanie
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #zmiana rozmiaru obrazu
img_streatch = cv2.resize(img, (600,600)) # rotacja z interpolacją pikseli
img_streatch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST) #rotacja bez interpolacji pikseli

cv2.imshow("Half", img_half)
cv2.imshow("Streatch", img_streatch)
cv2.imshow("Streatch near", img_streatch_near)

#rotacja
M = cv2.getRotationMatrix2D((0,0), -45, 1) # rotacja o -45 st. z punktu 0,0 obrazu
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
