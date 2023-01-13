#Reduce una lista a un solo valor
import functools #Viene en esta librería y solo devuelve un valor
numbers = [1,2,3,4]

def accum(counter,item):
  print('Counter:',counter)
  print('item:',item)
  return counter+item
  
result = functools.reduce(accum,numbers)
print(result)
