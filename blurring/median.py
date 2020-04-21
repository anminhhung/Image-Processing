import cv2
import imutils

image = cv2.imread("base.png")
image = imutils.resize(image, width=200)
cv2.imshow("Original", image)

for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Average {}".format(k), blurred)
    cv2.waitKey(0)