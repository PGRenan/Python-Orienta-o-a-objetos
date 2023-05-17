
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    #METODO 1
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    # METODO 2
    def deposita(self,valor):
        self.__saldo += valor


    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel_a_sacar

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    #METODO 4
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #METODO 5
    def get_saldo(self):
        return self.__saldo

    #METODO 6
    def get_titular(self):
        return self.__titular

    #METODO 7
    @property #chame sem parenteses
    def limite(self):
        return self.__limite

    #METODO 8
    @limite.setter #chame sem parenteses como se fosse uma atribuição
    def limite(self, limite):
        self.__limite = limite

    #METODO 9
    @staticmethod # chama com atribuição = Classe.nome_do_metodo()
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}
