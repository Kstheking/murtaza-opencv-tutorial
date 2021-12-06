import cv2
print("done")

# read image

img = cv2.imread('assets/girl.png')

cv2.imshow("Output", img)
cv2.waitKey(1000) #if 0 infnite wait else in ms

# read video

vid = cv2.VideoCapture("assets/vid.gif")

while True:
    success, img = vid.read()
    if(not success):
        break
    cv2.imshow("Video", img)
    if(cv2.waitKey(1) and 0xFF == ord('q')): # wait 1 ms and if q pressed then close the video
        break

# read webcam 

vid = cv2.VideoCapture(0) # id of webcam
vid.set(3, 640)
vid.set(4, 480)

while True:
    success, img = vid.read()
    if(not success):
        break
    cv2.imshow("Video", img)
    if(cv2.waitKey(1) & 0xFF == ord('q')): # wait 1 ms and if q pressed then close the video
        break