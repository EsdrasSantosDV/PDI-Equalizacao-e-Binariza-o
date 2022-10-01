
import cv2
import numpy as np
img = cv2.imread('./dado.jpg')

kernel = np.ones((5,5),np.uint8)  

abertura=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imwrite("abertura.jpg",abertura)


fechamento=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imwrite("fechamento.jpg",fechamento)

