import cv2
import numpy as np 
import imutils

image = cv2.imread("base.png")
image = imutils.resize(image, width=200)
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype = "uint8") * 200
added = cv2.add(image, M)
cv2.imshow("Added", image)

M = np.ones(image.shape, dtype = "uint8") * 100
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)