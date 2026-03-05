from produto import Produto
from carrinho import Carrinho
from caixa import Caixa

# --- CONFIGURAÇÃO DO SISTEMA (BANCO DE DADOS SIMULADO) ---
# Criação do estoque inicial com alguns produtos
estoque = {
    "001": Produto('Toddy', 8.50, '001', 10),
    "002": Produto('Leite', 4.20, '002', 5),
    "003": Produto('Pão', 0.50, '003', 50)
}

# Iniciando caixa com  valor de fundo de reserva
meu_caixa = Caixa(100.0)

def exibir_menu():
    print("\n" + "="*30)
    print("   CAIXA DE SUPERMERCADO   ")
    print("="*30)
    print("[1] Adicionar Produto")
    print("[2] Ver Carrinho")
    print("[3] Finalizar Compra")
    print("[4] Sair do Sistema")
    return input("Escolha uma opção: ")

# --- LOOP PRINCIPAL DE OPERAÇÃO ---
def rodar_sistema():
    carrinho_atual = Carrinho() # Inicia o primeiro carrinho
    
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            cod = input("Digite o código do produto: ")
            if cod in estoque:
                try:
                    qtd = int(input(f"Quantidade de {estoque[cod].nome}: "))
                    if qtd > 0:
                        carrinho_atual.adicionar(estoque[cod], qtd)
                    else:
                        print("Erro: A quantidade deve ser positiva.")
                except ValueError:
                    print("Erro: Digite um número inteiro válido.")
            else:
                print("Produto não cadastrado!")

        elif opcao == '2':
            carrinho_atual.ver_carrinho()

        elif opcao == '3':
            if not carrinho_atual.itens:
                print("Atenção: O carrinho está vazio!")
                continue
            
            # O caixa processa o pagamento
            if meu_caixa.processar_pagamento(carrinho_atual.total):
                carrinho_atual.exibir_cupom()
                print("\nVENDA FINALIZADA COM SUCESSO!")
                # Após finalizar, criamos um novo carrinho limpo para o próximo
                carrinho_atual = Carrinho()
            else:
                print("Pagamento não concluído. O carrinho continua aberto.")

        elif opcao == '4':
            print(f"\nEncerrando... Saldo Final em Caixa: R$ {meu_caixa.saldo:.2f}")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Garante que o sistema só rode se este arquivo for executado diretamente
if __name__ == "__main__":
    rodar_sistema()