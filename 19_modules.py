#Los módulos sirven para guardar el código en distintos archivos
import sys
print(sys.path)

import re #Tomar el curso de regulares de platzi
text = 'Mi número de teléfono es 482910493 el codigo del pais es 57,  mi número de la suerte es el 7'
result = re.findall('[0-9]+',text)
print(result)

import time
timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local)
print(result)

import collections 
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)