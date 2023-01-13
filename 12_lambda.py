def increment(x):
  return x +1

increment_v2 = lambda x:x+1 #Función que retorna un valor de acuerdo a la entrada

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name,last_name:f"Mi nombre completo es {name.title()} {last_name.title()}"

text = full_name('Bogdan','Rivera')
print(text)


  