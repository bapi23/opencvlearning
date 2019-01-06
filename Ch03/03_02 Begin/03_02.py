import numpy as np
import cv2


bw = cv2.imread("detect_blob.png", 0)
height, width = bw.shape[0:2]
cv2.imshow("Original", bw)

binary = np.zeros([height, width], 'uint8')

threshold = 85

for row in range(0, height):
    for col in range(0, width):
        if bw[row][col] > threshold:
            binary[row][col] = 255

ret, thresh = cv2.threshold(bw, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow("threshold", thresh)

cv2.imshow("Binary", binary)



cv2.waitKey(0)
cv2.destoryAllWindows()
