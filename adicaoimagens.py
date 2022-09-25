import cv2 
imagem1 = cv2.imread('./dado.jpg', 1) 
imagem2 = cv2.imread('./dado2.jpg', 1) 
img = cv2.add(imagem1, imagem2) 


cv2.imwrite("./adicaoimagens.jpg", img)