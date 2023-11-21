# Neste exemplo pretendo usar uma
# classe para implementar
# um iterador simples.

class MyIterator:
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor < self.limite:
            resultado = self.valor
            self.valor += 1
            return resultado
        else:
            raise StopIteration

# Nesse exemplo foi implementado
# a classe MyIterator
# que implementa o protocolo
# de iteração.

# O método __iter__ retorna
# o próprio objeto, pois
# ele é um iterador.

# O método __next__ retorna
# o próximo elemento da sequência
# e lança a exceção StopIteration
# quando não há mais elementos
# para serem iterados.

# O método __next__ é chamado
# quando a função next é chamada
# no objeto iterador.

# O método __iter__ é chamado
# quando a função iter é chamada
# no objeto iterador.

# O método __iter__ retorna
# o próprio objeto iterador
# e o método __next__ retorna
# o próximo elemento da sequência.

m = MyIterator(3)

print(next(m))
print(next(m))
print(next(m))
# print(next(m))

for i in m:
    print(i)
    
# Como o iterador já
# foi percorrido
# ele não tem mais
# elementos para serem
# iterados.