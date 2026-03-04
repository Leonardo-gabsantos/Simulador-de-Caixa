import uuid

print('--- Simulador de Caixa de Supermercado ---')

class Saldo:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
        print(f"Saldo inicial do caixa: R$ {self.valor:.2f}")

    def receber(self, quantia):
        self.valor += quantia
        print(f"Recebido: R$ {quantia:.2f} | Saldo em Caixa: R$ {self.valor:.2f}")

    def pagar(self, qtd):
        if qtd <= self.valor:
            self.valor -= qtd
            print(f"Pagamento realizado: R$ {qtd:.2f} | Saldo em Caixa: R$ {self.valor:.2f}")
        else:
            print(f"Erro: Saldo insuficiente para pagar R$ {qtd:.2f}")

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.token_id = uuid.uuid4()
        print(f"Cliente {self.nome} registrado. (ID: {str(self.token_id)[:8]}...)")

class Produto:
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.total_compra = 0

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        self.total_compra += produto.preco
        print(f"Item: {produto.nome} (R$ {produto.preco:.2f}) adicionado ao carrinho de {self.cliente.nome}")

    def finalizar(self, caixa):
        print(f"\n--- Finalizando compra de {self.cliente.nome} ---")
        print(f"Total a pagar: R$ {self.total_compra:.2f}")
        caixa.receber(self.total_compra)
        self.itens = [] 
        print("------------------------------------------\n")

meu_caixa = Saldo(100.0)


p1 = Produto('Toddy', 8.50, '001')
p2 = Produto('Leite', 4.20, '002')
p3 = Produto('Pão', 12.00, '003')


cliente_leonardo = Cliente("Leonardo")
carrinho_leo = Carrinho(cliente_leonardo)


carrinho_leo.adicionar_produto(p1)
carrinho_leo.adicionar_produto(p2)
carrinho_leo.adicionar_produto(p3)


carrinho_leo.finalizar(meu_caixa)

