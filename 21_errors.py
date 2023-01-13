#print(0/0)
#print(result) #El programa termina cuando se genera un error, no lo ejecuta
#Error de verificacion
print('Hola')
suma = lambda x,y:x+y
assert suma(2,2)==4 #Verifica un resultado en excepcion

print('Hola 2')

age = 10
if age<18:
  raise Exception('No se permiten menores de edad') #Se lanza un error
