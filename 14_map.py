#Hace transformaciones a una lista dada de elementos
numbers = [1,2,3,4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i*2)

numbers_v3 = list(map(lambda i:i*2,numbers))
#Transforma una lista de elementos y cumple la HOF

print("Numbers: ",numbers)
print("Numbers_v2: ",numbers_v2)
print("Numbers_v3:",numbers_v3)

numbers_1= [1,2,3,4]
numbers_2= [5,6,7]

print("Numbers_1:",numbers_1)
print("Numbers_2:",numbers_2)
result = list(map(lambda x,y:x+y,numbers_1,numbers_2))
print("Result:",result)