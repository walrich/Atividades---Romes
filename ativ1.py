#EXERCICIO 1

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é impar.')

par_ou_impar(int(input("Digite o número inteiro: ")))

#EXERCICIO 2
def multiplo_ou_nao(numero):
    if numero % 5 == 0:
        print(f'O número {numero} é multiplo de 5.')
    else:
        print(f'O número {numero} não é multiplo de 5.')

multiplo_ou_nao(int(input("Digite o numero inteiro: ")))

#EXERCICIO 3
def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False
    
def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False
    
numero = int(input("Digite o número inteiro: "))
if multiplo_de_5(numero) and multiplo_de_3(numero):
    print(f"O número {numero} é multiplo de 5 e de 3.")
elif multiplo_de_5(numero):
    print(f"O número {numero} é multiplo de 5.")
elif multiplo_de_3(numero):
    print(f"O número {numero} é multiplo de 3.")
else:
    print(f"O número {numero} não é multiplo de 5 e nem de 3.")

#EXERCICIO 4

def fibonacci(numero_de_elementos):
    if numero_de_elementos == 1:
        return 0
    elif numero_de_elementos == 2:
        return [0,1]
    else: 
        fibonacci = [0,1]
        for i in range(2,numero_de_elementos):
            novo_elemento_da_lista = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(novo_elemento_da_lista)
        return fibonacci
    
print(fibonacci(int(input("Digite a quantidade de números de Fibonacci que você"))))

#EXERCICIO 5

def checagem_multiplo_5(numero):
    if numero % 5 == 0:
        print(f"O número {numero} é múltiplo de 5.")
        return True
    else:
        print(f"O número {numero} não é múltiplo de 5.")
        return False
    
checagem_multiplo_5(numero)

#EXERCICIO 6

#Solicitar ao usuario inserir um numero inteiro positivo

def solicitar_numero():
    numero_inserido = int(input("Digite um número inteiro positivo: "))
    if numero_inserido == "":
        print("Você não digitou um número.")
        return solicitar_numero()
    if numero_inserido.isnumeric():
        print("Você não digitou um número.")
        return solicitar_numero()
    return int(numero_inserido)

