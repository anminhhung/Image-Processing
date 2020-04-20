import cv2
import imutils

image = cv2.imread("base.png")
image = imutils.resize(image, width=200)
cv2.imshow("Original", image)

#gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale", gray_img)

# yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
# cv2.imshow("YUV", yuv_image)

# cv2.imshow("Y channel", yuv_image[:,:,0])
# cv2.imshow("U channel", yuv_image[:,:,1])
# cv2.imshow("V channel", yuv_image[:,:,2])

g, b, r = cv2.split(image)

gbr_image = cv2.merge((g, b, r))
rbr_image = cv2.merge((r, b, r))

cv2.imshow('Original', image)
cv2.imshow('GRB', gbr_image)
cv2.imshow('RBR', rbr_image)


cv2.waitKey(0)