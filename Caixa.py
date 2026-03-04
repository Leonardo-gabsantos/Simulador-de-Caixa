import uuid

print('Simulador de caixa de supermercado')

class Saldo():
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
        print(f"Saldo inicial estabelecido em: R$ {self.valor:.2f}")

    def receber(self , quantia):
        self.valor += quantia
        print(f"Adicionado: R$ {quantia:.2f} | Saldo Atual: R$ {self.valor:.2f}")

    def pagar(self, qtd):
        self.subtrair = qtd
        print(f'Removido: R$ {qtd:.2f} | Saldo atual: R$ {self.valor - qtd}')

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.token_id = uuid.uuid4()
        print(f"Cliente {self.nome} criado com sucesso!")
        print(f"Token ID: {self.token_id}")
        
    
meucaixa = meu_caixa = Saldo(100.0)
meu_caixa.receber(50.50)
meu_caixa.pagar(20)

Cliente1 = Cliente("Leonardo")
Cliente2 = Cliente("Julia")
Cliente3 = Cliente("Gabriel")
Cliente4 = Cliente("Giovana")

print(Cliente1.nome)
print(Cliente2.nome)
print(Cliente3.nome) 

print(f'{Cliente4.nome} pagou: {meu_caixa.pagar(30)} reais')
print(f'{Cliente4.nome} recebeu: {meu_caixa.receber(30)} reais')
    


    
