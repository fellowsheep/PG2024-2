import numpy as np
import cv2 as cv

img = cv.imread('baboon.png') #original
imgResult = img.copy()
imgResult2 = img.copy()

print("Atributos da imagem",img.shape,"\n")

for i in range(img.shape[0]): #percorre linhas
	for j in range(img.shape[1]): #percorre colunas
		media = (img.item(i,j,0) + img.item(i,j,1) + img.item(i,j,2))/3.0
		imgResult.__setitem__((i,j,0),media) # canal B!!!!!!!!!!!!!!!!
		imgResult.__setitem__((i,j,1),media) # canal G
		imgResult.__setitem__((i,j,2),media) # canal R!!!!
		media = img.item(i,j,0) * 0.07 + img.item(i,j,1) * 0.71 + img.item(i,j,2) *0.21
		imgResult2.__setitem__((i,j,0),media) # canal B!!!!!!!!!!!!!!!!
		imgResult2.__setitem__((i,j,1),media) # canal G
		imgResult2.__setitem__((i,j,2),media) # canal R!!!!

cv.imshow("Imagem Original", img)
cv.imshow("Imagem Grayscale",imgResult)
cv.imshow("Imagem Grayscale Ponderado",imgResult2)

k = cv.waitKey(0)