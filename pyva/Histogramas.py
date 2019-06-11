#histogramas escala de grises

from matplotlib import pyplot as plt
# pip3 install matplotlib
#import matplotlib._version
#print(matplotlib.__version__)   #3.0.3
import cv2

# loading and converting the image into numpy array
rutaFoto0="foto0.jpg"
image = cv2.imread(rutaFoto0)


# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)
cv2.waitKey(0)

# create the histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

#plot the graph
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("bins")
plt.ylabel("No of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)

#########################
#HISTOGRAMAS ECUALIZACIÓN
# mejora el contraste de una imagen expandiendo la distribución de píxeles
# se aplica sobre escala de grises
# se usa para mejorar fotografías. Por ejemplo: rayos x
import numpy as np

# loading and converting the image into numpy array
image = cv2.imread(rutaFoto0)

# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)
cv2.imshow("Normal and Equilized",np.hstack([gray, eq]))
cv2.waitKey(0)


#####################
#IMAGE BLURRING
# el desenfoque de la imagen significa que cada píxel de la imagen se mezcla con las 
# intensidades de píxeles que lo rodean
# es útil cuando se procesan imágenes
# Las funciones de visión de computadora, como el trenzado y la detección de bordes, 
# funcionan mejor si la imagen primero se suaviza o difumina.

# loading and converting the image into numpy array
image = cv2.imread(rutaFoto0)

#average blurring
# 
#Defina una ventana deslizante k * k (kernel) en la parte superior de nuestra imagen, 
# donde k siempre es un número impar.
# Esta ventana va a deslizarse de izquierda a derecha y de arriba a abajo.
# El píxel en el centro de esta matriz se configura para que sea el promedio de todos los 
# demás píxeles que lo rodean.
# A medida que aumenta el tamaño del kernel, la imagen más borrosa se volverá
blurred = np.hstack([
	cv2.blur(image, (3,3)),
	cv2.blur(image, (5,5)),
	cv2.blur(image, (7,7))])

cv2.imshow("averaged blurr", blurred)
cv2.waitKey(0)

#gaussian blurring
# similar a average blurring, pero usa una media ponderada
# Los píxeles del vecindario que están más cerca del píxel central contribuyen más al promedio.
# el resultado final es que nuestra imagen es menos borrosa, pero más naturalmente borrosa
# que usando el método average
blurred = np.hstack([
	cv2.GaussianBlur(image, (3,3), 0),
	cv2.GaussianBlur(image, (5,5), 0),
	cv2.GaussianBlur(image, (7,7), 0)])

cv2.imshow("Gaussian blurr", blurred)
cv2.waitKey(0)

#median blurring
# El método de desenfoque mediano ha sido más efectivo al eliminar el ruido de sal y pimienta.
# A diferencia del método averaging, en vez de reemplazar el pixel central con la media de los
# de los vecinos, reemplazamos el pixel central con la mediana de los vecinos
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])

cv2.imshow("Median blurr", blurred)
cv2.waitKey(0)

#bilateral blurring
# Con el fin de reducir el ruido mientras se mantienen los bordes, podemos utilizar el 
# difuminado bilateral.
# este método es capaz de preservar los bordes de una imagen, mientras reduce el ruido
# El mayor inconveniente de este método es que es considerablemente más lento que el promedio,
# el gauss y la distorsión media.
# el primer parámetro es la imagen, el segundo es el diámetro de nuestro píxeles vecinos,
# el tercero es color
# finalmente, el espacion q. Un valor mayor significa que píxeles más lejanos del píxel central
# influirá en el cálculo del borronado
blurred = np.hstack([
	cv2.bilateralFilter(image, 3, 21, 21),
	cv2.bilateralFilter(image, 5, 31, 31),
	cv2.bilateralFilter(image, 7, 41, 41)])

cv2.imshow("bilateral blurr", blurred)
cv2.waitKey(0)

###################
# IMAGE THRESHOLD
# thresholding es la binarización de una imagen
# es convertir una imagen en escala de grises a una imagen binaria, donde los píxeles 
# son 0 o 255
# un ejemplo sería seleccionar un valor de píxel p, y luego configurar todas las intensidades 
# de píxel menores que p a cero, y todos los valores de píxel mayores que p a 255

# loading and converting the image into numpy array
image = cv2.imread(rutaFoto0)

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
# aplica gaussianblur con un ro de 5 radius
# este filtro elimina algunos de los bordes de la imagen que no interesan
blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Gaussian blurr", blurred)

#simple Thresholding using binary
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

#simple Thresholding using inv binary
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Inv Binary", threshInv)

cv2.imshow("Only Coins", cv2.bitwise_and(image, image, mask = threshInv))


#adaptive thresholding using mean
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive mean", thresh)

#adaptive thresholding using gaussian
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive gaussian", thresh)

cv2.waitKey(0)
