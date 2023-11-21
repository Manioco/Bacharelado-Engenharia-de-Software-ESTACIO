# Como no exemplo anterior
# uso a mesma classe MyIterator
# mas agora ela entra em loop
# quando não há mais elementos
# para serem iterados.

# Ainda existirá a exceção
# StopIteration, mas ela será
# lançada quando o iterador
# for reiniciado.

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
            self.valor = 0
            raise StopIteration
        

m = MyIterator(3)

# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

for i in m:
    print(i)

for i in m:
    print(i)