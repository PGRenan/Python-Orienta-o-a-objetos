class Cliente:

    def __init__(self, nome):
        self.__nome = nome

#como visto anteriormente, para chamar o atributo é necessario chamar o objeto.atributo, e quando ele esta privado, deve se chamar o objeto._class__atributo (onde o __atributo é o atributo privado)

    @property
    def nome(self):
        #isso é um meio de criar um get sem um get na frente
        print("Chamando @property nome()")
        #.title(), torna a primeira letra maiuscula
        return nome.title()
#com o @property, faz com que vc posssa chamar o metodo sem precisar o parenteses, dizendo para o sistema que esse metodo é um apropriedade, dessa forma, se coloca no nome do metodo o mesmo nome do atributo, e quando fachamos a o obijeto.atributo ao inves de retrornar apenas o atributo, será executrado o metodo

    @nome.setter
    def nome(self, nome):
        print("chamendo setter nome()")
        self.__nome = nome
# com @nome.setter, podemos fezer parecido com o property, onde nos setamso um nome, sem precisar de um set, e podemos subistituir o nome com um comando mais simples, cliente.nome = "marco
#antes cliente.set_nome("nome").....  depois cliente.nome = "marco"