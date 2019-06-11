#DETECCIÓN DE GRADIENTE DE IMAGEN
# el gradiente de una imagen en escala de grises corresponde a las regiones en forma de borde 
# en las direcciones x e y
# Es un cambio direccional en la intensidad del color en una imagen.
# detercar bordes es una de la operaciones fundamentales que puedes hacer en procesamiento de
# imágenes. Ayuda a reducir el volumen de datos (píxeles) a procesar y mantienen el aspecto
# estructural de una imagen

import numpy as np
import cv2

rutaFoto0="foto0.jpg"
# loading and converting the image into numpy array
image = cv2.imread(rutaFoto0)

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# laplace gradient detection
# Función para calcular la magnitud del gradiente.
# la transición de negro a blanco es considerado como pendiente positiva
# la transición de blanco a negro es pendiente negativa
lap = cv2.Laplacian(image, cv2.CV_64F)

#convert back to 8 bit unsigned int
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplace Gradient Detection", lap)


# Sobel X and Y
# los dos últimos parámetros son el orden de las derivadas en las direcciones x e y
# especifica un valor 1 y 0 para encontrar bordes verticales
# especifica un valor 0 y 1 para encontrar bordes horizontales
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

#convert back to 8 bit unsigned int
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("Sobel X", sobelX)
cv2.imshow("Sobel Y", sobelY)
cv2.imshow("Sobel Combined", sobelCombined)

cv2.waitKey(0)

#####################
#DETECCIÓN DE BORDE INTELIGENTE
# es un proceso de varios pasos:
# incluye: distorsionar la imagen para eliminar ruido;
#          Soltel gradient images en la dirección x y en la y para eliminar bordes
#          un proceso de histeresis que determina si un píxel es borde o no
# argumentos: la imagen en gris distorsionada
#             dos valores, threshold1 y threshold2
#                   cualquier valor gradiente mayor que threshold2 es edge
#                   cualquier valor por debajo de threshold1 no es edge
#                   cualquier valor intermedio habrá que fijar un criterio

# loading and converting the image into numpy array
image = cv2.imread(rutaFoto0)

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Gaussian blurr", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edge Detected", canny)
cv2.waitKey(0)

#######################
#CONTORNO/PERÍMETRO DE IMÁGENES
# en una imagen las "curvas" son llamadas contornos
# contorno: curva de puntos sin espacios en dicha curva.
# contornos son muy útiles para cosas como aproximación de imagen y análisis
# loading and converting the image into numpy array
# loading and converting the image into numpy array
image = cv2.imread(rutaFoto0)

# convert image to greyscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(gray, (15,15), 0)

cv2.imshow("Gaussian blurr", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edge Detected", canny)

# finding the contours, counting and marking them
# encuentra los contornos de las figuras y los cuenta
# el primer argumento es la edge imagen
# el segundo argumento es el tipo de contornos que queremos. En este caso los contornos más externos
# el tercer argumento es cómo queremos aproxima el contorno
(cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("The number of coins in the image is : {}".format(len(cnts)))

#create a copy of the image
coins = image.copy()

# draw the contours in the actual color image copy
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Contours", coins)

cv2.waitKey(0)



