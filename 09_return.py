def find_volume(lenght=1,width=1,depth=1):
  return lenght*width*depth,width,'hola' #Retorna varios parámetros y retorna una tupla

#Si se le pone valor desde un inicio se puede utilizar simplemente con la función sin parámetros


result,widht,text = find_volume(width=10,lenght=20)
print(result)
print(widht)
print(text)
