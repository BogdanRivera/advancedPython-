#Un iterador es un objeto que permite recorrer uno a uno los elementos almacenados en una estructura de datos, y operar con ellos

for i in range(1,10):
  print(i)

my_iter = iter(range(1,4))
print("Primero: ",my_iter)
print(next(my_iter)) #Se puede hacer ua iteracion con la palabra reservada next
print(next(my_iter)) #Se itera manualmente por cada next
print(next(my_iter))
#No se está generando un array de 10 elementos si no que lo va generando progresivamente y por ende el recurso de memoria no es tan alto y lo hace a medida de que ingresa el iterador
#Algo a tener en cuenta que en algún momento va a llegar al límite y genera una excepcion


