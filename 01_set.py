#Los conjuntos son tipos de datos que tienen una característica en común
#No se pueden repetir más de dos veces un elemento del conjunto 
#Se aplican casi igual que los diccionarios pero sin las Keys
set_countries = {'col','mex','bol','col'} #Se duplicó el elemento. Forma explicita
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,443,23}
print(set_numbers)

set_types = {1,'hola',False,12.12}
print(set_types)

set_from_string = set('hola') #Apartir de la palabra hola se separan las letras en posiciones del set
print(set_from_string)

set_from_tuples = set(('abc','cbv','as','abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
#Toma unicamente los valores únicos
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

