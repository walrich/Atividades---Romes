
# Estudo dirigido de revisão da unidade A. As atividades valem um ponto extra para a prova. Cada exercício deverá ser feito em um arquivo separado, com o nome do arquivo sendo o nome da função. Por exemplo, o exercício 1 deverá ser feito no arquivo multiplo_de_5.py, o exercício 2 deverá ser feito no arquivo multiplo_de_5_e_3.py, e assim por diante.

# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário.

def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número inteiro: "))

if multiplo_de_5(numero):
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")

### Duas linhas de código

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} é múltiplo de 5." if numero % 5 == 0 else f"O número {numero} não é múltiplo de 5.")

    
# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.

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


    

# Exercício 3: Crie um programa em que o usuário insira uma palavra e o programa retorna se a palavra é palíndromo ou não.

# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.

# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.

raio = int(input("Digite o raio do círculo: "))

def calcular_area(raio):
    area = (raio ** 2) * 3.14
    print(f'A área do circulo é {area} m2')

def calcular_perimetro(raio):
    perimetro = 2 * 3.14 * raio
    print(f'O perimetro do ciruclo é {perimetro} m')

calcular_area(raio)
calcular_perimetro(raio)


# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.

ano = int(input("Digite o ano que você nasceu: "))
if ano in [2020,2008,1996,1984,1972,1960]:
    print("Seu signo é Rato!")
elif ano in [2021,2009,1997,1985,1973,1961]:
    print("Seu signo é Boi!")
elif ano in [2010,1998,1986,1974,1962,1950]:
    print("Seu signo é Tigre!")
elif ano in [2011,199,1987,1975,1963,1951]:
    print("Seu signo é Coelho!")
elif ano in [2012,2000,1988,1976,1964,1952]:
    print("Seu signo é Dragão!")
elif ano in [2013,2001,1989,1977,1965,1953]:
    print("Seu signo é : Serpente!")
elif ano in [2014,2002,1990,1978,1966,1954]:
    print("Seu signo é Cavalo!")
elif ano in [2015,2003,1991,1979,1967,1955]:
    print("Seu signo é Cabra!")
elif ano in [2016,2004,1992,1980,1968,1956]:
    print("Seu signo é Macaco!")
elif ano in [2017,2005,: 1993,1981,1969,1957]:
    print("Seu signo é Galo!")
elif ano in [2018,2006,1994,1982,1970,1958]:
    print("Seu signo é Cão!")
elif ano in [2019,2007,1995,1983,1971,1959]:
    print("Seu signo é Porco!")

: 
# Exercício 7: Faça um programa que solicita ao usuário inserir um número inteiro e retorna se ele é primo.

# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10. Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.: 
