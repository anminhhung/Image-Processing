import numpy as np
import cv2

'''
    initialize on cavas as a 400x400 with 3 channels
    Red, Green, Blue with a black background
'''
canvas = np.zeros((400, 400, 3), dtype='uint8')

# draw yellow line from top-left connor to bottom-right connor
yellow = (255, 255, 0)
cv2.line(canvas, (0, 0), (400, 400), yellow)
cv2.imshow("Demo", canvas)
cv2.waitKey(0)

# draw a 4 thick red line from top-right connor to bottom-left
red = (0, 0, 255)
cv2.line(canvas, (400, 0), (0, 400), red, 4)
cv2.imshow("Demo", canvas)
cv2.waitKey(0)

# draw a green 50x50 pixel square, starting at 10x10 and ending at 60x60
green = (0, 255, 0)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Demo", canvas)
cv2.waitKey(0)

# draw another rectangle, starting at 50x150 and ending at 150x225
# make it white and 5 pixels thick.
white = (255, 255, 255)
cv2.rectangle(canvas, (50, 150), (150, 225), white, 5)
cv2.imshow("Demo", canvas)
cv2.waitKey(0)

# draw last rectangle, starting at 200x50 and ending at 225x125
# make it blue and fill in.
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Demo", canvas)
cv2.waitKey(0)

# draw a yellow circle at the center of the canvas with r = 30 pixels.
r = 30
cv2.circle(canvas, (200, 200), r, yellow)
cv2.imshow("Demo", canvas)
cv2.waitKey(0)