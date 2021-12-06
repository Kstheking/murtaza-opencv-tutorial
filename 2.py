import cv2

img = cv2.imread("assets/girl.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cvt i.e. convert color , BGR being default color code in 
# cv2 
imgBlur = cv2.GaussianBlur(img, (7, 7), 0) # src ksize sigmaX

cv2.imshow("Output", imgGray)

cv2.waitKey(1000)

cv2.imshow("Output", imgBlur)

cv2.waitKey(1000)