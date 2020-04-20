import cv2 
import numpy as np

# using 2 functions like cv2.add and cv2.subtract
add = cv2.add(np.uint8([200]), np.uint8([100]))
sub = cv2.subtract(np.uint8([50]), np.uint8([150]))

print("max of 255: {}".format(str(add)))
print("min of 0: {}".format(str(sub)))

# using numpy array
add = np.uint8([200]) + np.uint8([100])
sub = np.uint8([50]) - np.uint8([150])

print("wrap around: {}".format(str(add)))
print("wrap around: {}".format(str(sub)))