import imutils
import cv2

image = cv2.imread("base.png")

shifted_1 = imutils.translate(image, 50, 100)
shifted_2 = imutils.translate(image, -50, -100)

cv2.imshow("Shifted Right-Down", shifted_1)
cv2.imshow("Shifted Left-Up", shifted_2)
cv2.waitKey(0)