with open('./text.txt','w+') as file:
  for line in file:
    print(line)
  file.write('Nueva cosas en este archivo\n') 
  file.write("Otra  línea\n")
  file.write('Más línea\n')

#como este comando solo es para leer. Esto es por defecto en el comando open. Si agregamos una 'W' entonces será de escritura. open('./text.txt','w')
#Se debe tener cuidado porque nos dice que no es un archivo de lectura y puede eliminar todo el contenido del archivo
#Si se le agrega r+ entonces tendremos los permisos necesarios tanto de lectura como de escritura
#Se puede hacer el salto de línea como \n
#En el caso de r+ lo lee y se puede manipular pero en el caso de w+ lo manipula y lo sobreescribe todo el archivo