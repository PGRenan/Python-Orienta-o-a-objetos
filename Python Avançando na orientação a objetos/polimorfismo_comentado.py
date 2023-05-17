
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome= novo_nome.title()

    def __str__(self):
        return(f"{self._nome} - {self.ano} - {self._likes}")

    #def imprime(self):
    #    print(f"{self._nome} - {self.ano} - {self._likes}")


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return(f"{self._nome} - {self.ano} - {self.duracao} min - {self._likes}")


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


    def __str__(self):
        return(f"{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}")

#Objeto - Class FIlme
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()

#Objeto - Class Serie
atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()




filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    #com esse __str__ quando damos print, o python vai printar todos os textos de cada classe
    print(programa)
    #com o imprime() criado em cada um das clases, sera varrido o imprime em todas as classes e sera imprimido de maneira correta
    #programa.imprime()