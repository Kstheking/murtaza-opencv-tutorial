import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("assets/girl.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cvt i.e. convert color , BGR being default color code in 
# cv2 
imgBlur = cv2.GaussianBlur(img, (7, 7), 0) # src ksize sigmaX

imgCanny = cv2.Canny(img, 150, 200) # edges

imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)

imgErosion = cv2.erode(imgDialation, kernel, iterations = 1)

cv2.imshow("Output", imgGray)

cv2.waitKey(1000)

cv2.imshow("Output", imgBlur)

cv2.waitKey(1000)

cv2.imshow("Output", imgCanny)

cv2.waitKey(1000)

cv2.imshow("Output", imgDialation)

cv2.waitKey(1000)

cv2.imshow("Output", imgErosion)

cv2.waitKey(1000)