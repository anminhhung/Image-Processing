import cv2
import imutils

image = cv2.imread("base.png")
image = imutils.resize(image, width=200)
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv2.imshow("Blurred d={}, sc={}, ss={}".\
            format(diameter, sigmaColor, sigmaSpace), blurred)
    cv2.waitKey(0)