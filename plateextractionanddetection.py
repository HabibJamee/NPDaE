
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt


img = cv2.imread('File name',cv2.IMREAD_COLOR)

img = cv2.resize(img, (620,480) )

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
edged = cv2.Canny(gray, 30, 200) #Perform Edge detection

cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
implot=plt.imshow(img)
plt.show()
implot=plt.imshow(gray)
plt.show()
implot=plt.imshow(edged)
plt.show()




for c in cnts:
 
 peri = cv2.arcLength(c, True)
 approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
 
 if len(approx) == 4:
  screenCnt = approx
  break
if screenCnt is None:
  detected = 0
  print ("No contour detected")
else:
  detected = 1

if detected == 1:
 cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

imgplot= plt.imshow(img)
plt.show()
imgplot= plt.imshow(edged)
plt.show()




mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)
imgplot= plt.imshow(new_image)
plt.show()




(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]
imgplot= plt.imshow(Cropped)
plt.show()



Cropped = cv2.resize(Cropped, (620,480) )

cv2.imwrite( 'cropped1.png', Cropped )
