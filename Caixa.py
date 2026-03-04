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
    
meucaixa = meu_caixa = Saldo(100.0)
meu_caixa.receber(50.50)
meu_caixa.pagar(20)



    


    
