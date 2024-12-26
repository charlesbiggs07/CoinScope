import cv2

img = cv2.imread('Images/img.png')

img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img2gray, 10,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
c = max(contours, key=cv2.contourArea )
print(c)
cv2.drawContours(img, contours, -1, (0,0,255), 1)

cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()