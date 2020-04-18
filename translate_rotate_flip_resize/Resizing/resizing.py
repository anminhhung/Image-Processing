import cv2

image = cv2.imread("base.png")

#resized = cv2.resize(image, (350, 150))

# calculating the ratio based on width.
# let's make our new image have a width of 200 pixels.
# r = 200.0 / image.shape[1]
# dim = (200, int(image.shape[0] * r))

# calculating the ratio based on height
# let's make the height of the resized image 100 pixels.
r = 100.0 / image.shape[0]
dim = (int(image.shape[1] *r ), 100)


# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Resizing", resized)
cv2.waitKey(0)