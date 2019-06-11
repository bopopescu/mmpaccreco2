import numpy as np
import cv2 as cv
import utilidades as uts
'''
def trasladar(imagen, x, y):
    M = np.float32([[1,0,x], [0,1,y]])
    desplazada = cv.warpAffine(imagen, M, (imagen.shape[1], imagen.shape[0]))
    return desplazada
'''

rutaBalon="balon.jpg"
cv.imshow("uso desplazar versión NumPy",uts.desplazarNP(rutaBalon,100.0,0.0))
cv.waitKey(0)