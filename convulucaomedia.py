import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./dado.jpg')
plt.imshow(img)
plt.show()
  

median_blur = cv2.medianBlur(src=img, ksize=9)
  
plt.imshow(median_blur)
plt.show()