import cv2 as cv
import utilidades as uti
import imutils as iu

rutaBalon="balon.jpg"
imagen = cv.imread("balon.jpg")
#el segundo parámetro mueve la imagen de izqda a dcha con valor positivo
#                                     de dcha a izqda con valor negativo
#el tercer parámetro mueve la imagen de arriba a abajo con valor positivo
#                                    de abajo a arriba con valor negativo
#deplaza hacia abajo 100px
desplazar = iu.translate(imagen, 0, 100)
cv.imshow("imagen trasladada hacia abajo",desplazar)
cv.waitKey(0)
#desplaza hacia arriba 100px
desplazar = iu.translate(imagen, 0, -100)
cv.imshow("imagen trasladada hacia arriba",desplazar)
cv.waitKey(0)
#desplaza hacia izquierda 100px
desplazar = iu.translate(imagen, -100, 0)
cv.imshow("imagen trasladada hacia izquierda",desplazar)
cv.waitKey(0)
#desplaza hacia derecha 100px y abajo 50px
desplazar = iu.translate(imagen, 100, 50)
cv.imshow("imagen trasladada hacia arriba",desplazar)
cv.waitKey(0)


#rotar imagen usando imutils
cv.imshow("roto 180 grados",iu.rotate(uti.leeImagen(rutaBalon),180))
cv.waitKey(0)
#rotar imagen usando NP
cv.imshow("roto 45 usando NP",uti.rotarNP(rutaBalon,45,None,1))
cv.waitKey(0)

#redimensionar versión imutils
cv.imshow("redimensiono imutils",iu.resize(uti.leeImagen(rutaBalon),width=800))
cv.waitKey(0)
#redimensioanr versión NumPy
cv.imshow("redimension usand NP",uti.redimensionarNP(rutaBalon,None,800))
cv.waitKey(0)

#ahora viene flip
#flip 0
cv.imshow("flip 0",cv.flip(uti.leeImagen(rutaBalon),0))
cv.waitKey(0)
#flip 1
cv.imshow("flip 1",cv.flip(uti.leeImagen(rutaBalon),1))
cv.waitKey(0)
#flip -1
cv.imshow("flip -1",cv.flip(uti.leeImagen(rutaBalon),-1))
cv.waitKey(0)

#crop - recortar una imagen <---> utilidades.porcionImagen
uti.mostrarImagen("imagen original",rutaBalon)
cv.imshow("imagen recortada",uti.porcionImagen(rutaBalon,15,222,150,400))
cv.waitKey(0)