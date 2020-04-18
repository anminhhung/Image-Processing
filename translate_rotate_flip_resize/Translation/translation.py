import cv2 
import numpy as np
import imutils

image = cv2.imread("base.png")
num_rows, num_cols = image.shape[:2]

# let's translate the image 50 pixels to the right and 100 pixels down
#translation_matrix = np.float32([[1, 0, 50], [0, 1, 100]])
translation_matrix = np.float32([[1, 0, -50], [0, 1, -100]])
shifted = cv2.warpAffine(image, translation_matrix, (num_cols, num_rows))

cv2.imshow("Translation", shifted)
cv2.waitKey(0)