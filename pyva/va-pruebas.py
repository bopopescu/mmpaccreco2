import cv2
import utilidades as u
#print(cv2.__version__)  #4.0.1

imagen = cv2.imread("balon.jpg")
#print(imagen.shape[0])  #426 el alto
#print(imagen.shape[1])   #639 el ancho
'''
def getWidthImage(ruta:str)->int:
    return cv2.imread(ruta).shape[1]
'''
ruta="balon.jpg"
#print(u.getWidthImage(ruta))    #639
#print(u.getHeightImage(ruta))   #426
#print(u.numChannels(ruta))      #3
u.mostrarImagen("m2ps",ruta)    #sí lo hace
#u.guardaImagen("nuevo.jpg",ruta)    #sí lo hace

(b,g,r) = imagen[0,0]   #píxel 0,0 <--->R:172,G:169,B:152
print("píxel 0,0 - Red: {}, Green: {}, Blue: {}".format(r,g,b)) #172,169,152
w0=200
w1=500
h0=50
h1=350
porcion = imagen[h0:h1, w0:w1]
#alto,ancho
cv2.imshow(f"{h0}:{h1}, {w0}:{w1}",porcion)
cv2.waitKey(0)
#con esto selecciona una porción y le pone color
imagen[h0:h1,w0:w1]=(0,255,0)
cv2.imshow("balón verde",imagen)
cv2.waitKey(0)

#u.porcionImagen("hola",ruta,h0,h1,w0,w1)
u.muestraPorcionImagen("hola",ruta,h0,h1,w0,w1)

