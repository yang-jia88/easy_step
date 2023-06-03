import cv2
import numpy as np

img = cv2.imread("terria.png")
# h,w,c=img.shape #高 寬 顏色
# print(h,w,c)
# newimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# h1,w1 = newimg.shape
# print(h1,w1)

hueimage = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lowRange = np.array([7, 3, 14])
#highRange = np.array([5, 255, 255])
highRange = np.array([80, 29, 60])
# 網路上的人認為是紅色的區域

mask = cv2.inRange(img, lowRange, highRange) #把符合標成白色
cv2.imshow('mask', mask)
res = cv2.bitwise_and(img, img, mask=mask) #其他去掉
cv2.imshow('Input', img)
cv2.imshow('Result', res)
while cv2.waitKey(100) != 27: #27 is esc ascii code
    if cv2.getWindowProperty("Input",cv2.WND_PROP_VISIBLE)<=0:
        break

img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img[10][0])