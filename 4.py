import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

img[:] = 255,0,0 # blue image

cv2.imshow("Output", img)

cv2.waitKey(1000)

cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)

cv2.imshow("Output", img)

cv2.waitKey(1000)

cv2.rectangle(img, (0, 0), (250, 250), (0, 0, 255), 2) # in place of 2 you can write cv2.FILLED and it will fill the rectangle

cv2.imshow("Output", img)

cv2.waitKey(1000)

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv2.imshow("Output", img)

cv2.waitKey(1000)

cv2.putText(img, "hey bruh what's up", (200, 50), cv2.FONT_ITALIC, 1, (0, 0, 0), 1)

cv2.imshow("Output", img)

cv2.waitKey(1000)