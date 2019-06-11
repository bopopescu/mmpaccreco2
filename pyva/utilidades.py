import cv2
import numpy as np
#aunque aparece unresolved imports, funciona
import imutils as iu    

def leeImagen(ruta:str):
    return cv2.imread(ruta)
'''
obtiene la anchura de una imagen a partir de la ruta de dicha imagen
'''
def getWidthImage(ruta:str)->int:
    return leeImagen(ruta).shape[1]
    #return cv2.imread(ruta).shape[1]

'''
obtiene la altura de una imagen a partir de la ruta de dicha imagen
'''
def getHeightImage(ruta:str)->int:
    return leeImagen(ruta).shape[0]
    #return cv2.imread(ruta).shape[0]

def numChannels(ruta:str)->int:
    return leeImagen(ruta).shape[2]


def mostrarImagen(nombreImagen,ruta:str):
    cv2.imshow(nombreImagen,leeImagen(ruta))
    cv2.waitKey(2000)

def guardaImagen(nombre,ruta:str):
    cv2.imwrite(nombre,leeImagen(ruta))

def porcionImagen(ruta,h0,h1,w0,w1):
    return leeImagen(ruta)[h0:h1,w0:w1]

def muestraPorcionImagen(nombre,ruta,h0,h1,w0,w1):
    cv2.imshow(nombre,porcionImagen(ruta,h0,h1,w0,w1))
    cv2.waitKey(0)

def getCanvas(altura,anchura,canales,tipo):
    return np.zeros((altura,anchura,canales),dtype=tipo)

#desplaza una imagen usando NumPy
def desplazarNP(imagen, x, y):
    imagen=leeImagen(imagen)
    M = np.float32([[1,0,x], [0,1,y]])
    return cv2.warpAffine(imagen, M, (imagen.shape[1], imagen.shape[0]))

def rotarNP(imagen, angulo, centro=None, escala=1.0):
    imagen=leeImagen(imagen)
    (altura,anchura)=imagen.shape[:2]
    if centro is None:
        centro=(anchura//2,altura//2)
    M=cv2.getRotationMatrix2D(centro,angulo,escala)
    return cv2.warpAffine(imagen, M, (anchura,altura))

def redimensionarNP(imagen,anchura=None,altura=None,inter=cv2.INTER_AREA):
    dimensiones= None
    imagen=leeImagen(imagen)
    (anch,altu)=imagen.shape[:2]
    if anchura is None and altura is None:
        return imagen
    if anchura is None:
        r = altu/float(altura)
        dimensiones=(int(anch*r),altura)
    else:
        r = anchura/float(anch)
        dimensiones=(anchura,int(altu*r))
    return cv2.resize(imagen,dimensiones,interpolation=inter)

