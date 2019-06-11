import numpy as np
import cv2
from PIL import Image
import matplotlib
'''
im1 = np.array(Image.open("imagen0.jpg")).astype(np.int) # cast to ints
im2 = np.array(Image.open("imagen0.jpg")).astype(np.int)
difference = im1 - im2 # if you do this with uint8 arrays the negative values will wrap i.e. (0, 2, 2) - (1, 4, 2) => (255, 254, 0)
diff = np.where(np.abs(difference) > THRSHLD)[0] # np.where will return a tuple of 1D arrays
diff_count = len(diff) # react if more than N pixel_colours have changed enough
'''

0

import cv2
import numpy as np
a = cv2.imread("imagen0.jpg")
#b = cv2.imread("imagen0.jpg")  #iguales
b = cv2.imread("imagen4.jpg")   #no son iguales Da pete
difference = cv2.subtract(a, b)    
result = not np.any(difference)
if result is True:
    print("Pictures are the same")
else:
    print("Pictures are different")