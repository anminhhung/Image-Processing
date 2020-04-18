import cv2
import imutils

image = cv2.imread("base.png")

rotated = imutils.rotate(image, 180, scale=0.7)

cv2.imshow("Rotation", rotated)
cv2.waitKey(0)