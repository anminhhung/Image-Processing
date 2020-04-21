import cv2

image = cv2.imread("text.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# apply a list of erosions
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow("Dilated {} times".format(i+1), dilated)
    cv2.waitKey(0)