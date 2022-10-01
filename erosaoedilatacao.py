
import cv2
import numpy as np
img = cv2.imread('./dado.jpg')

kernel = np.ones((3,3),np.uint8)  

erosao=cv2.erode(img,kernel,iterations=14)

cv2.imwrite("erosao.jpg",erosao)


dilatacao=cv2.dilate(img,kernel,iterations=14)

cv2.imwrite("dilatacao.jpg",dilatacao)