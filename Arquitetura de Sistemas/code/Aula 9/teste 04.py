

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
            # Desse modo ele gera
            # um NONE e reinicia
            # o iterator, criando
            # um loop infinito
            self.valor = 0 
        

m = MyIterator(3)

# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

tempo = 10
for i in m:
    tempo -= 1
    if tempo <=0:
        break
    else:
        print(i)
