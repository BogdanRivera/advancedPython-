'''
numbers = []
"""
Se crea un elemento y se guardan las iteraciones en el conjunto de numeros
"""
for element in range(1,11):
  numbers.append(element*2)

print(numbers)
#De una manera más sencilla
numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)
'''

#Con condicionales
numbers = []
for i in range(1,11):
  if i%2 == 0:
    numbers.append(i*2)

print(numbers)

numbers_v2 = [i*2 for i in range(1,11) if i%2==0]
print(numbers_v2)


prueba_numbers = [i for i in range (1,21) if (i%2)!=0]
print(prueba_numbers)


