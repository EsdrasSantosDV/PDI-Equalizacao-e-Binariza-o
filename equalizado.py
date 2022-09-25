from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread("./dado.jpg")
(img_B, img_G, img_R) = cv2.split(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)
cv2.imwrite("./imagemequal.jpg", h_eq)

h_eq_B = cv2.equalizeHist(img_B)
h_eq_G = cv2.equalizeHist(img_G)
h_eq_R = cv2.equalizeHist(img_R)
h_eq_BGR = cv2.merge([h_eq_B, h_eq_G, h_eq_R])
cv2.imwrite("./imagemequalizadargb.jpg", h_eq_BGR)

#Separa os canais
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
canais = cv2.split(h_eq_BGR)#(img_H, img_S, img_V)
for (canal, c) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0, 256])
img_eq_gray = cv2.cvtColor(h_eq_BGR, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./imagem_eq_gray.jpg", img_eq_gray)
hist = cv2.calcHist([img_eq_gray], [0], None, [256], [0, 256])
plt.plot(hist, color = "y")
plt.show()



plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

#img = cv2.imread('wiki.jpg',0)
#equ = cv2.equalizeHist(img)
#res = np.hstack((img,equ)) #stacking images side-by-side
#cv2.imwrite('res.jpg',res)

cv2.waitKey(0)