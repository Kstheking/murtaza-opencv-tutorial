import cv2
import numpy as np

img = cv2.imread('assets/girl.png')

print(img.shape) # shape of the image (height, width, number of channels)

cv2.imshow("Output" ,img)

cv2.waitKey(1000)

imgResize = cv2.resize(img, (500, 1200)) # width, height

cv2.imshow("Output" ,imgResize)

cv2.waitKey(1000)

imgCropped = img[0:500, 0:200] 

cv2.imshow("Output", imgCropped)

cv2.waitKey(1000)