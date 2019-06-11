#a partir de una imagen obtengo las caras que hay. Creo una imagen con cada cara
#personas2.jpg tiene 5 caras, así que creo 5 imágenes jpg
import cv2
print(cv2.__version__)
from PIL import Image
import numpy as np
import dlib 
print(dlib.__version__)
import face_recognition as fr

rutaPersonas="personas2.jpg"

# loading and converting the image into numpy array
image = cv2.imread(rutaPersonas)

# Find all the faces in the image using the library
face_locations = fr.face_locations(image)

# printing the number of items in the array
print("I found {} face(s) in this photograph".format(len(face_locations)))
i=0
for face_location in face_locations:

	#print location of each face in this image
	top, right, bottom, left = face_location
	print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

	#access and show each face in the image
	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	nombreImagen="imagen"+str(i)+".jpg"
	print(nombreImagen)
#	pil_image.save(nombreImagen)
	i=int(i)+1
#	pil_image.show()