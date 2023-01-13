set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

"""Unión"""
set_c = set_a.union(set_b)
print(set_c)

print(set_a | set_b) #La barra '|' significa una unión. No hay diferencia entre el método de 'union'

"""Intersección"""
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a&set_b)  #El simbolo '&' significa una intersección. No hay diferencia entre el método de 'intersection'

"""Diferencia"""
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b) #El simbolo '-' significa una diferencia. No hay diferencia entre el método de 'diference'

"""Diferencia simétrica"""
#Es como una union pero sin tener el elemento en común entre ellos
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a^set_b)


