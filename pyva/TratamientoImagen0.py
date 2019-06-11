#MÁSCARA
# permite poner el foco en las porciones de la ima que no interesa. Por ejemplo: una cara
#es la misma imagen pero con valor blanco en los que pasan el filtro y color negro 
# los pixeles que no.
import numpy as np
import cv2

# loading and converting the image into numpy array
rutaBalon="balon.jpg"
image = cv2.imread(rutaBalon)
cv2.imshow("Balon Original", image)
cv2.waitKey(0)

# create numpy array filled with zeros with exact width and height of image
# create a rectangular mask
# zeros son píxeles negros
# unos son píxeles blancos
# un píxel está apagado si tiene valor cero
# un píxel está encendido si tiene valor mayor que cero
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Máscara Rectangular", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Imagen Mascarada", masked)
cv2.waitKey(0)

# create numpy array filled with zeros with exact width and height of image
# create a circular mask
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Máscara Circular Blanca", mask)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Máscara de imagen circular", masked)
cv2.waitKey(0)

#########
#image color channels merging and splitting

# loading and converting the image into numpy array
image = cv2.imread(rutaBalon)
#cv2.imshow("Original", image)
#cv2.waitKey(0)

#split the image based on channels
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)


#alternate method
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

#merge back the channels
merged = cv2.merge([B, G, R])
cv2.imshow("merged", merged)
cv2.waitKey(0)


#otros espaciones de colores

# loading and converting the image into numpy array
image = cv2.imread(rutaBalon)
cv2.imshow("BGR Color Space", image)
cv2.waitKey(0)

# BGR to GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)

# BGR to HSV
# hue saturation value <---> es cómo humanos ven el color
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# BGR to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

cv2.waitKey(0)


