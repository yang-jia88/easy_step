import cv2
import numpy as np

blank = np.zeros((500,500,3),dtype = "uint8")
cv2.imshow("black",blank)


blank[200:400,100:200] = 0,0,255

cv2.imshow("other",blank)
cv2.waitKey(0)