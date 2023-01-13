set_countries = {'col','mex','bol','col'}
size = len(set_countries) #Tamaño del conjunti
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#Adicionar
set_countries.add('pe') #Agrega un elemento
print(set_countries)

#Actualizar un conjunto
set_countries.update({'ar','ecua','pe'}) #Es similar a Add con la diferencia que se pueden agregar mas elementos como los conjuntos
print(set_countries)

#Remove
set_countries.remove('col') #Elimina ese elemento
print(set_countries)

#set_countries.remove('arg') #Elimina ese elemento pero no maneja excepcion

set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

set_countries.clear() #Limpia todo el conjunto
print(len(set_countries)) #Tamaño del conjunto

