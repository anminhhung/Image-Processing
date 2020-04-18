import cv2
import imutils

image = cv2.imread("base.png")

methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

# loop over the interpolaton methods
for (name, method) in methods:
    # increase the size of the image by 1.2x 
    resized = imutils.resize(image, width=int(image.shape[1]*1.2), inter=method)
    cv2.imshow("Original", image)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)