import cv2
import numpy as np 

image = cv2.imread("base.png")
cv2.imshow("Original", image)

# construct a rectangle mask that displays only the person in the image
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (284, 77), (556, 360), 255, -1)
#cv2.imshow("mask", mask)

# Apply our mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to image", masked)
cv2.waitKey(0)