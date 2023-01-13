items = [
  {
  'product' : 'camisa',
  'price' : 100,
  },
  {
  'product':'pantalones',
  'price':300
  },
  {
  'product':'pantalones2',
    'price':200
  }
  
]

prices = list(map(lambda item: item['price'],items))
print("Precios:",prices)
#En esta funcion agrega la variable taxes al diccionario, se puede cambiar el nombre
def add_taxes(item):
  item['taxes'] = item['price']*.19
  return item

new_items = list(map(add_taxes,items))
print(new_items)

#Hay cambios en la variable original  con MAP
#new_items = list(map(add_taxes,items))
#print(new_items)

def add_iva(item,x):
 item['iva'] = item['price']*x
 return item
x = [0.16,0.16,0.16]

#prueba = list(map(add_iva,items,x))
#print("Prueba:",prueba)




