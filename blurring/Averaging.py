import cv2
import imutils

image = cv2.imread("base.png")
image = imutils.resize(image, width=200)
cv2.imshow("Original", image)

kernel_sizes = [(3, 3), (9, 9), (15, 15)]

for (x, y) in kernel_sizes:
    blurred = cv2.blur(image, (x, y))
    cv2.imshow("Average ({}, {})".format(x, y), blurred)
    cv2.waitKey(0)