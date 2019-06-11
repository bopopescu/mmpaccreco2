#dice si 2 imágenes son iguales, si no son la imagen, peta
from PIL import Image
import numpy as np

im1 = np.array(Image.open("imagen0.jpg"))
#im2 = np.array(Image.open("imagen0.jpg"))  #al comparar im1 y im2 usando imagen0.jpg, "The images are the same"
im3 = np.array(Image.open("imagen4.jpg"))   #al comparar im1 e im3 ValueError: operands could not be broadcast together with shapes (52,52,3) (62,62,3) 
difference = im1 - im3
if np.all(difference == 0): # more readable than 'not np.any'
  print("The images are the same")
else:
  print("IMÁGENES DIFERENTES")
  '''
  Image.fromarray(difference[:,:,:3].astype(np.uint8))'''