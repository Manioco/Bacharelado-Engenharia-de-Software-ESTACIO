
# Nesse teste eu verifico que o Iterator
# retorna o erro StopIteration
# quando não há mais elementos
# para serem iterados na lista.

a = [0,1,2]

iterator = iter(a)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
