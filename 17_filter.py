numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x:x%2==0,numbers))
print(new_numbers)
#La función filter no modifica ningún atributo de la lista original, a diferencia de lo que pasa con MAP



