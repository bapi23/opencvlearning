import numpy as np
import cv2
from collections import namedtuple
import math

Circle = namedtuple("Circle", "x, y, radius, color")

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
circles = []

start_x = 0
start_y = 0
radius = 0

drawing = False

# click callback
def click(event, x, y, flags, param):
	global canvas
        global circles
        global start_x
        global start_y
        global drawing
        radius = math.sqrt((abs(x - start_x)**2 + abs(y - start_y)**2))

	if event == cv2.EVENT_LBUTTONDOWN:
		print("LButton Down")
                start_x = x
                start_y = y
                drawing = True
	elif event == cv2.EVENT_MOUSEMOVE:

            if(drawing == True):
                canvas = np.ones([500,500,3],'uint8')*255
                cv2.circle(canvas, (start_x, start_y), int(radius), (0,0,255), 5) 

	elif event == cv2.EVENT_LBUTTONUP:
                c = Circle(start_x, start_y, int(radius), (0,0,255))
                circles.append(c)
                drawing = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:
        for circle in circles:
            cv2.circle(canvas, (circle.x, circle.y), circle.radius, circle.color, 5) 
	cv2.imshow("canvas",canvas)
        
	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	

cv2.destroyAllWindows()
