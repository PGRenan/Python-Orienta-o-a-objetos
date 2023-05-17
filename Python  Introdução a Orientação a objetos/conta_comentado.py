#class na orientação a objetos, o class é uma especie de receita de bolo, para o objeto, ou seja, num onjeto conta, tem que ter uma receita nome, saldo, limite e etc por exempo
# o uso do class é importante, por apos a criação do objeto, ele só sera valido, uma vez que, tiver toda a receita


#Dentro do class, é sempre necessario chamar uma função construtora, dessa forma é chamado o def __init__(self):, que serve para construir o objeto
#self é a referencia que encontra nosso objeto na memória
#self. siginifica, mandar o self ir pro "endereço", onde encontrar o objeto, criar os atributos, nesse caso os atrributos são numero, titular, saldo, limite.
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
#a utilização dos __ no atributi, é para restringir o atributo, deixa-lo privado, de forma que so se possa acessalos a partir dos metodos criados


#dessa forma, as funções extrato, deposita e saca são chamadas de metodo, que é um função diferente da costrutora, mas dentro do class.

    #METODO 1
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    # METODO 2
    def deposita(self,valor):
        self.__saldo += valor

    # METODO 3 e 3.5
# privando metodos, o metodo pode sacar, nor retorn true ou false e ele esta sendo usado apenas com objetivo de deixar mais legivel o metodo saca, e vericiar o limite, dessa forma pode-se privar o metodo assim como é feito com o atributo, para o usuario n utilizar livremente
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

#para a execução destes da classe, é necessario referenciar o objeto em uma referencia como, conta= Conta(123, "Nico", 55.5, 1000.0), desta forma a referencia se torna o objeto.

#para puxar as informações do estrato devesse pedir a patir de um objeto, ou seja, o objeto conta, da seguinte forma, conta.extrato() e conta.saca(10.0)

#caso vc utilise esse objeto em outra referencia, como, ref2= conta, esse objeto é copiado podendo buscar as informações dos metodos apartir de qualquer uma das duas referencias.

#caso queira limpar a referencia ref2= None, referencia limpa.

    #METODO 4
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
# dessa forma pode ser tranferido um valor de uma conta para outra, note que quando usamos self.saca(valor), o self esta chamando um metodo dessa vez, de forma que ele ao fazer o metodo, ele altera o atributo.
#o self, se refere a referencia pedia logo, conta2(trafere(10,conta), self esta se referindo a conta2


    #METODO 5
    def get_saldo(self):
        return self.__saldo
#normalmente é necessario sempre ter um metodo que devolve os seus atributos, normalmente usado para relatorios, por nomenclatura, é usado get_atributo como nome destes metodos
#metodos get sempre tem um return

    #METODO 6
    def get_titular(self):
        return self.__titular

# Quando precisamos mudar um valor de um atributo, usamos set_atributo como nomenclarura, como set é usado para modificar algo, n precusa de return
# Set deve ser usado com sabedoria, apenas quando for necessário, numero da conta e titular não mudam, o saldo, é modificado pelos metodos deposita, saca, e transfere, mas o limite, ele não é somado ou subtraido, ele é setado(escolhido), entçao faz sentido o Set



    #METODO 7
    @property#chame sem parenteses
    def limite(self):
        return self.__limite

    #METODO 8
    @limite.setter #chame sem parenteses como se fosse uma atribuição
    def limite(self, limite):
        self.__limite = limite
    #aqui podemos ver mais um exemplo de @property e @limite.setter, substituindo o get e set

    #METODO 7
    #def get_limite(self):
        #return self.__limite

    # METODO 8
    #def set_limite(self, limite):
        #self.__limite = limite

    #METODO 9
    @staticmethod # chama com atribuição = Classe.nome_do_metodo()
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}
    #@staticmethod é usado quando temos um metodo fixo, que n muda