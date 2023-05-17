
class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome= novo_nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome= novo_nome.title()

#Objeto - Class FIlme
vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
#Aqui cemos dois modos de usar o format, podemos usar apos a string, com .format(o que for preencer), ou com um simples f antes da string, e o que for preenchido dentro das chaves
vingadores.dar_like()
print("Nome: {} - Ano: {} - Duração: {} - Likes: {}".format(vingadores.nome, vingadores.ano, vingadores.duracao, vingadores.likes))
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes {vingadores.likes}")
#Objeto - Class Serie
atlanta = Serie("Atlanta", 2018, 2)
#Aqui cemos dois modos de usar o format, podemos usar apos a string, com .format(o que for preencer), ou com um simples f antes da string, e o que for preenchido dentro das chaves
atlanta.dar_like()
print("Nome: {} - Ano: {} - Temporadas: {} - Likes: {}".format(atlanta.nome, atlanta.ano, atlanta.temporadas, atlanta.likes))
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes {atlanta.likes}")