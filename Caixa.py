class Caixa:
    def __init__(self, saldo_inicial):
        
        self.saldo = saldo_inicial

    def processar_pagamento(self, total):
        """
        Gerencia a escolha da forma de pagamento e atualiza o saldo do caixa.
        Retorna True se o pagamento foi bem-sucedido e False se houve erro.
        """
        print(f"\n--- PAGAMENTO ---")
        print(f"VALOR TOTAL DA COMPRA: R$ {total:.2f}")
        print("1. Dinheiro")
        print("2. Cartão (Crédito/Débito)")
        
        opcao = input("Escolha a forma de pagamento: ")
        
        if opcao == '1':
            return self._pagamento_dinheiro(total)
        elif opcao == '2':
            return self._pagamento_cartao(total)
        else:
            print("[!] Opção de pagamento inválida.")
            return False

    def _pagamento_dinheiro(self, total):
        """Lógica interna para receber dinheiro e dar troco."""
        try:
            valor_entregue = float(input("Valor entregue pelo cliente: R$ "))
            
            if valor_entregue >= total:
                troco = valor_entregue - total
                self.saldo += total
                if troco > 0:
                    print(f"Troco a devolver: R$ {troco:.2f}")
                return True
            else:
                print(f"[!] Erro: Valor insuficiente. Faltam R$ {total - valor_entregue:.2f}")
                return False
        except ValueError:
            print("[!] Erro: Por favor, digite um valor numérico válido.")
            return False

    def _pagamento_cartao(self, total):
        """Simula a comunicação com a maquininha de cartão."""
        print("Processando cartão...")
        
        self.saldo += total
        print("Pagamento AUTORIZADO!")
        return True