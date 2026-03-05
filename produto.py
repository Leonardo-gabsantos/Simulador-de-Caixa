class Produto:
    def __init__(self, nome, preco, codigo, quantidade):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo
        self.quantidade = quantidade

    def __str__(self):
       return f"{self.nome} (R$ {self.preco:.2f}) - Estoque: {self.quantidade}"