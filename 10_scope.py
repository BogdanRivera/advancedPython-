price = 100 #Tiene un alcance global 
result = 200

def increment():
  price = 200
  result = price + 100
  print(result)
  return result
  
print(price)
price_2 = increment()
print(price_2)
print(result)

