# Importação das bibliotecas
import cv2
from matplotlib import pyplot as plt
# Leitura da imagem com a função imread()
imagem = cv2.imread('./dado.jpg')


img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #converte P&B
#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])


plt.hist(img.ravel(),256,[0,256])
plt.show()