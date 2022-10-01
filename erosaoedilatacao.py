
import cv2
import numpy as np
img = cv2.imread('./dado.jpg')

kernel = np.ones((5,5),np.uint8)  

erosao=cv2.erode(img,kernel,iterations=1)

cv2.imwrite("erosao.jpg",erosao)
#

dilatacao=cv2(img,kernel,iterations=1)

cv2.imwrite("dilatacao.jpg",dilatacao)