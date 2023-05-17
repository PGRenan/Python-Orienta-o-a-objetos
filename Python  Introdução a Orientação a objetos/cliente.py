
class Cliente:

    def __init__(self, nome):
        self.__nome = nome


    @property
    def nome(self):
        print("Chamando @property nome()")
        return nome.title()


    @nome.setter
    def nome(self, nome):
        print("chamendo setter nome()")
        self.__nome = nome
