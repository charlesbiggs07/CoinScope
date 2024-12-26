import cv2
import numpy as np

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# fontScale
fontScale = 1
# Blue color in BGR
color = (255, 0, 0)
# Line thickness of 2 px
thickness = 2

img = cv2.imread("Images/coins_01.jpg")
img = cv2.resize(img, (640, 800))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray, (17,17), 0)

circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=5, maxRadius=400)
#print(len(circles[0]))
#print(circles[0][0][0])
for circle in circles:
    for (x,y,r) in circle:
        print(x,y,r)
        cv2.circle(img, (int(x),int(y)), int(r), (0,255,0), 5)
        if r > 50:
            # org
            org = (int(x), int(y))
            # Using cv2.putText() method
            img = cv2.putText(img, 'Quarter', org, font,
                                fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()