import numpy as np
import cv2
import utilidades as u

rutaBalon="balon.jpg"
u.mostrarImagen("imagen original",rutaBalon)
#cv2 tiene como rango de valores de 0 a 255
n1=np.uint8([200])
n2=np.uint8([500])  ##500 lo representa como 244
print(n1," + ",n2," = ",cv2.add(n1,n2))
print("ahora n2 = 255. Salió 255 y sumó 255")
n2=np.uint8([300])  #lo pone como 44
print(n1," + ",n2," = ",cv2.add(n1,n2)) #244
#voy a sumar 200 + 100
n2=np.uint8([100])
print(n1," add ",n2," = ",cv2.add(n1,n2)) #255
print("ahora sumo ",n1," + ",n2," = ",n1+n2) 

print("ahora n1=50 y n2=100")
n1=np.uint8([50])
n2=np.uint8([100])
print("subtract ",cv2.subtract(n1,n2))  #0
print(" - ",n1-n2)  #206

#ahora voy a añadir a la imagen 
imagen=u.leeImagen(rutaBalon)
#np.ones genera una matriz de 1s, es decir, 
# hace que la imagen se vuelva blanca
M=np.ones(imagen.shape,dtype="uint8")*200
cv2.imshow("imagen add 1s",cv2.add(imagen,M))
cv2.waitKey()
#ahora hago lo contrario, se vé oscuro
M=np.ones(imagen.shape,dtype="uint8")*200
cv2.imshow("imagen subtract 1s",cv2.subtract(imagen,M))
cv2.waitKey()

