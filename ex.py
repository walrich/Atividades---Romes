#Fila de clientes
fila = []
#Dados clientes
dados = "dados_clientes.txt"

#Adicionar clientes na fila
def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    prioridade = input("Tem prioridade? (S/N)")
    cliente = {
        "Cliente": nome
        "Tem prioridade?": prioridade
    }
    fila.append(cliente)
    print("Cliente adicionado na fila com sucesso!")

def visualizar_fila():
    if not fila:
        print("A fila está vazia")
    else:
        print("Fila de clientes:")
        for cliente in fila:
            print(
                f"Cliente: {cliente['Cliente']}, Prioridade: {cliente['Tem prioridade?']}"
            )

#MENU
while True:
    print("\n Opções")
    print(
        "1. ADICIONAR CLIENTE A FILA \n2. VIZUALIZAR FILA \n3. ENCERRAR O SISTEMA"
        
    )
    opcao = input("ESCOLHA UMA OPÇÃO: ")
    if opcao == "1":
        adicionar_cliente()
    elif opcao == "2":
        visualizar_fila()
    elif opcao == "3":
        print("Sistema encerrado com sucesso!")
        break
    else:
        print("Opção inválida, tente novamente!")