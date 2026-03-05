class Carrinho:
    def __init__(self):
        # Lista que guardará dicionários com os dados dos itens
        self.itens = []
        self.total = 0

    def adicionar(self, produto, qtd):
        """Adiciona um produto ao carrinho e abate do estoque."""
        if produto.quantidade >= qtd:
            self.itens.append({
                'produto': produto.nome, 
                'preco': produto.preco, 
                'qtd': qtd
            })
            self.total += produto.preco * qtd
            produto.quantidade -= qtd  # Baixa no estoque do objeto produto
            print(f"-> {qtd}x {produto.nome} adicionado com sucesso!")
        else:
            print(f"Erro: Estoque insuficiente! (Disponível: {produto.quantidade})")

    def ver_carrinho(self):
        """Lista os itens atuais sem finalizar a compra."""
        if not self.itens:
            print("\n[!] O carrinho está vazio.")
            return
        
        total_volumes = sum(item['qtd'] for item in self.itens)
        print("\n--- CONTEÚDO DO CARRINHO ---")
        for i, item in enumerate(self.itens, 1):
            subtotal = item['qtd'] * item['preco']
            print(f"{i}. {item['qtd']}x {item['produto']} | Unitário: R$ {item['preco']:.2f} | Sub: R$ {subtotal:.2f}")
        
        print(f"----------------------------")
        print(f"Qtd. Itens: {total_volumes}")
        print(f"Total Parcial: R$ {self.total:.2f}")

    def exibir_cupom(self):
        """Gera o texto final após o pagamento."""
        print("\n" + "*"*28)
        print("       CUPOM FISCAL       ")
        print("*"*28)
        for item in self.itens:
            print(f"{item['qtd']}x {item['produto']:<15} R$ {item['preco']*item['qtd']:>6.2f}")
        print("-" * 28)
        print(f"TOTAL PAGO:       R$ {self.total:>6.2f}")
        print("*" * 28)