#Referencia de memoria cuando se realiza con diccionarios, se hace una modificacion porque ocupan la misma referencia de memoria

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
print(prices)
#En esta funcion agrega la variable taxes al diccionario, se puede cambiar el nombre
def add_taxes(item):
  #Se puede resolver de esta manera
  new_item=item.copy()
  new_item['taxes'] =item['price']*.19
  return new_item

new_items = list(map(add_taxes,items))
print('New list')
print(new_items)
print('Old list')
print(items)

#Hay cambios en la variable original  con MAP
#new_items = list(map(add_taxes,items))
#print(new_items)





