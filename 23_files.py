file = open('./text.txt')
#print(file.read()) #Lee todo el archivo
#print(file.readline()) #Funciona como un iterador y lee linea por linea
#print(file.readline())
#print(file.readline())
#print(file.readline())

#Realizando una iteracion con un for
for line in file:
  print(line) #Lo leemos linea a linea y no usa mucha memoria
  
file.close() #Cierra el archivo y libera espacio de memoria

#Esto funciona para que no se nos olvide el cerrar el archivo
with open('./text.txt') as file:
  for line in file:
    print(line)


