import cv2

image = cv2.imread("text.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

kernel_size = [(3, 3), (5, 5), (7, 7)]

# apply a list of erosions
for size in kernel_size:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Opening: ({}, {})".format(size[0], size[1]), opening)
    cv2.waitKey(0)