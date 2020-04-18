import cv2
import imutils 

image = cv2.imread("base.png")

resized_width = imutils.resize(image, width=200)
resized_height = imutils.resize(image, height=100)

cv2.imshow("Resized_width", resized_width)
cv2.imshow("Resized_height", resized_height)
cv2.waitKey(0)