import numpy as np
import cv2 as cv

#img = cv.imread('baboon.png') #original
img = cv.imread('baboon.png') #original
print("Atributos da imagem",img.shape,"\n")
imgResult = img.copy()
imgColored = img.copy()
imgInverted = img.copy()
mColor = [255, 0, 255]

R, G, B = cv.split(img)


imgTest = cv.cvtColor(img, cv.COLOR_BGR2HSV)
H, S, V = cv.split(imgTest)
scale = 1.2
S = np.clip(S * scale, 0, 255).astype(np.uint8)  # Convertendo para uint8
imgTest = cv.merge([H, S, V])
imgTest = cv.cvtColor(imgTest, cv.COLOR_HSV2BGR)

img2 = cv.imread('bolinhas.png') #original
imgResult2 = img2.copy()

imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
print("Atributos da imagem",imgGray.shape,"\n")

for i in range(img.shape[0]): #percorre linhas
	for j in range(img.shape[1]): #percorre colunas
		imgResult.__setitem__((i,j,0),img.item(i,j,0)) # canal B!!!!!!!!!!!!!!!!
		imgResult.__setitem__((i,j,1),img.item(i,j,0)) # canal G
		imgResult.__setitem__((i,j,2),img.item(i,j,0)) # canal R!!!!
		imgColored.__setitem__((i,j,0),img.item(i,j,0) | mColor[0]) # canal B!!!!!!!!!!!!!!!!
		imgColored.__setitem__((i,j,1),img.item(i,j,1) | mColor[1]) # canal G
		imgColored.__setitem__((i,j,2),img.item(i,j,2) | mColor[2]) # canal R!!!!
		imgInverted.__setitem__((i,j,0),img.item(i,j,0) ^ 255) # canal B!!!!!!!!!!!!!!!!
		imgInverted.__setitem__((i,j,1),img.item(i,j,1) ^ 255) # canal G
		imgInverted.__setitem__((i,j,2),img.item(i,j,2) ^ 255) # canal R!!!!
		
for i in range(img2.shape[0]): #percorre linhas
	for j in range(img2.shape[1]): #percorre colunas
		imgResult2.__setitem__((i,j,0),img2.item(i,j,0)) # canal B!!!!!!!!!!!!!!!!
		imgResult2.__setitem__((i,j,1),img2.item(i,j,0)) # canal G
		imgResult2.__setitem__((i,j,2),img2.item(i,j,0)) # canal R!!!!

cv.imshow("Imagem Original", img)
#cv.imshow("Canal R - Babuino",imgResult)
#cv.imshow("Canal R - Bolinhas",imgResult2)
cv.imshow("Saturation",imgTest)
cv.imshow("Grayscale (cvtColor)",imgGray)
cv.imshow("Colorizada",imgColored)
cv.imshow("Inversão",imgInverted)

k = cv.waitKey(0)