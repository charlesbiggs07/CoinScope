import cv2
import numpy as np

img = cv2.imread('Images/coins_01.jpg')
img = cv2.resize(img, (640, 800))
image_copy = img.copy()
#img = cv2.GaussianBlur(img, (7,7), 3)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 85, 255, cv2.THRESH_BINARY)
print(len(threshold))
contours,_ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)




cv2.imshow("IMG", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()