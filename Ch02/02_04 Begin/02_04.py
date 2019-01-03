import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image",0,0)
b, g, r = cv2.split(color)
rgb_split = np.concatenate((r,g,b), axis=1)
cv2.imshow("Split", rgb_split)

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("hsvSplit", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()
