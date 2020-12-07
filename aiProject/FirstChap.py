import cv2
import numpy as np
print("Package succesfully imported")

#so to play around with images use the class cv2 and include/import in the project this package: OPENCV
#read images from the folder
img = cv2.imread("data/imgone.jpg")
#print(img.shape) #print the dimension of the picture
#imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #add effects

#display the image
cv2.imshow("Import img",img)

#cv2.imshow("Black and white colors",imgg)
cv2.waitKey(0)


imf = np.zeros((500,500)) #create an output image matrix with given dimession
print(imf.shape)

cv2.line(img,(0,0), (300,300), (0,255,0), 3)




