

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    contra["saldo"] += valor

def saca(conta, valor):
    contra["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))