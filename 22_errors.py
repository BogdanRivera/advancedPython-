#Manejando las excepciones de este modo el programa no se interrumpe y puede seguir su curso normal
try:
  print(0/0)
  assert 1!=1, 'Uno no es igual que uno'
  age = 10
  if age<18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
  
  
print('Hola')

#Se pueden ejecutar varios try con except en uno solo
"""
age = 10
try:
  assert age>18, "No se permite la entrada a menores de edad"
except Exception as error:
  print(error)
"""