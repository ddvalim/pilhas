class Pilha:
    def __init__(self, limite):
        self.__pilha = []
        self.__limite = limite

    def pilha_vazia(self):
        return len(self.__pilha) == 0

    def pilha_cheia(self):
        return len(self.__pilha) == self.__limite

    def numero_elementos(self):
        return len(self.__pilha)

    def top(self):
        if len(self.__pilha) != 0:
            return self.__pilha[-1]
        else:
            raise Exception("Pilha vazia")

    def pop(self):
        if len(self.__pilha) != 0:
            return self.__pilha.pop()
        else:
            raise Exception("Pilha vazia")

    def push(self, elemento: int):
        if len(self.__pilha) <= self.__limite:
            self.__pilha.append(elemento)
        else:
            raise Exception("Pilha cheia")


s = Pilha(6)
s.push(3)
s.push(4)
s.push(7)
top = s.top()
print(top)
s.pop()
top = s.top()
print(top)