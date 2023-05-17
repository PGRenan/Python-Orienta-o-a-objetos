
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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

#define que essa classe é interavel
    def __getitem__(self, item):
        return self._programas[item]

#para fazer listagem
    @property
    def listagem(self):
        return self._programas

#para fazer len
    def __len__(self):
        return len(self._programas)


#Objeto - Class FIlme
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores_dois = Filme("vingadores_dois", 2019, 160)
atlanta = Serie("atlanta", 2018, 2)
atlanta_dois = Serie("atlanta_dois", 2019, 2)


vingadores.dar_like()
atlanta_dois.dar_like()
vingadores_dois.dar_like()
atlanta.dar_like()
vingadores_dois.dar_like()
atlanta_dois.dar_like()
vingadores.dar_like()
atlanta.dar_like()




filmes_e_series = [vingadores, atlanta, vingadores_dois, atlanta_dois]

playlist_fim_de_semana = Playlist('Playlist fim de semana', filmes_e_series)

print(f'Tamando da playlist: {len(playlist_fim_de_semana)}')

print(playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana:
    print(programa)

#Inicialização __init__
#Reoresentação __str__, __repr__
#Container, sequancia __contains__, __iter__, __len__, __getitem__
#Numericos __add__, __sub__, __mul__, __mod__