# Importação das bibliotecas
from matplotlib import pyplot as plt
import numpy as np
import cv2
img = cv2.imread('./dado.jpg')
#Separa os canais
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
canais = cv2.split(img)#(img_H, img_S, img_V)
for (canal, c) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0, 256])
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist, color = "y")
plt.show()