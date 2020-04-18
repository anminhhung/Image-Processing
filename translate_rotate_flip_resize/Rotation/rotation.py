import cv2
import numpy as np 

image = cv2.imread("base.png")
num_rows, num_cols = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 0.7)
image_rotation = cv2.warpAffine(image, rotation_matrix, (num_cols, num_rows))

cv2.imshow("rotation", image_rotation)
cv2.waitKey(0)