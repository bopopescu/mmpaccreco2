import cv2 as cv
import numpy as np
import utilidades as ut
#un canvas de 300px de altura y 300px de anchura y con 3 canales y cuyo tipo es uint8
#canvas = np.zeros((303,303,3),dtype="uint8")
canvas=ut.getCanvas(300,300,3,"uint8")
#color rojo
red=(0,0,255)
#línea con origen 0,0 y fin 300,300 y con color rojo
cv.line(canvas,(0,0),(300,300),red)
#muestro la imagen
cv.imshow("línea 1",canvas)
cv.waitKey(0)

green=(0,255,0)
#el último parámetro, el 10, marca la anchura de la línea
cv.line(canvas,(0,0),(300,300),green,10)
cv.imshow("línea 2",canvas)
cv.waitKey(0)

#un rectángulo
cv.rectangle(canvas,(10,10),(60,60), red)
cv.imshow("rectángulo 1",canvas)
cv.waitKey(0)

cv.rectangle(canvas,(10,10),(60,60), red, 3)
cv.imshow("rectángulo 2",canvas)
cv.waitKey(0)

blue=(255,0,0)
#anchura -1 quiere decir que el rectángulo tiene relleno de color azul
cv.rectangle(canvas,(10,10),(60,60), blue, -1)
cv.imshow("rectángulo 3",canvas)
cv.waitKey(0)

#un círculo
cv.circle(canvas,(100,100),100, red)
cv.imshow("círculo 1", canvas)
cv.waitKey(0)