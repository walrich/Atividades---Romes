## LISTA DE REPOSTAS PYHTON                             FACULDADES IESGO                                           ALUNO: LUAN BRITO SOUSA CALAZANS | BSI 1°SEM | 1° LISTA DE EXERCICIOS 

##                  LEMBRANDO QUE OS PROBLEMAS DEVEM SER COPIADOS UNICAMENTE E ABERTO EM OUTRO.PY PARA RODAR  

## EXERCICIO 1 :
def  troca_vogal():
    palavra = input(" digite a palavra que queira trocar as vogais ") 
    return palavra.replace("a","*").replace("e","*").replace("i","*").replace("o","*").replace("u","*").upper() + f"\n a palavra que você escolheu foi : {palavra}"
    
print(troca_vogal())
##____________________________________________________________________________________________________________________________________________________________________
## EXERCICIO 2 :

def contador_caracters():
    palavra_frase = input('digite a palavra / frase. ')
    print('a frase escolhida foi: '+ palavra_frase)
    print("ela possui tantos caracters" , len(palavra_frase));

print(contador_caracters())
##____________________________________________________________________________________________________________________________________________________________________
## EXERCICIO 3 :

def contador_de_a():
    nome = input('digite seu nome: ')
    return f"A letra 'A' aparece {nome.count('a')+nome.count('A')} vezes."
print(contador_de_a())
##____________________________________________________________________________________________________________________________________________________________________
##EXERCICIO 4 : 

def letra_maisculas():
    nome = input('digite seu nome completo : ')
    return nome.title()
print(letra_maisculas())
##____________________________________________________________________________________________________________________________________________________________________
##EXERCICIO 5 :

def letra_minusculas():
    nome = input('digite seu nome completo : ')
    return nome.lower()
print(letra_minusculas())
##____________________________________________________________________________________________________________________________________________________________________
## EXERCICIO 6 :

def nomemaiusculo_sobrenomeminusculo():
    nome = input('digite nome e sobrenome : ')  
    primeiro_nome = nome.split()[0]
    ultimo_nome = nome.split()[-1]
    return f"O seu primeiro nome é {primeiro_nome.upper()} ,E o seu Sobrenome é {ultimo_nome.lower()}"

print(nomemaiusculo_sobrenomeminusculo())
##____________________________________________________________________________________________________________________________________________________________________
##EXERCICIO 7 :

def nome_sobrenome():
    nome_usuario = input("digite seu nome e sobrenome: ")
    sobrenome_usuario = input("digite somente seu sobrenome: ")
    nome_completo = input("digite seu nome completo : ").upper()
    tamanho_nome_completo = len(nome_completo)
    return f"Seu nome e sobrenome é :{nome_usuario}, Seu ultimo nome é :{sobrenome_usuario}\n Seu nome completo é :{nome_completo.lower()}, e possui :{tamanho_nome_completo} caracters."

print(nome_sobrenome())
##____________________________________________________________________________________________________________________________________________________________________
##EXERCICIO 8 : 
def menu_1():
    palavra = input("digite a frase. Contador de palavras. ")
    contador = palavra.split()
    contador2 = len(contador)
    print("Sua frase possui " , contador2 , 'palavras.') 

def menu_2():
    vogal = input("Conta Vogais. ")
    print("A volgal 'A' aparece: ", vogal.count('a')+vogal.count('A') ,"Vezes.")
    print("A vogal 'E' aparece:" , vogal.count('e')+vogal.count('E') , "Vezes.")
    print("A vogal 'I' aparece:" , vogal.count('i')+vogal.count('I') , "vezes.")
    print("A vogal 'O' aparece:", vogal.count('o')+vogal.count('O'), "vezes.")
    print("A vogal 'U' aparece:", vogal.count('u')+vogal.count('U'), "vezes.")

def menu_3():
    substituir = input('troca palavra: Python~Java ')
    print(substituir.replace('python','Java').replace('Python','Java').replace('PYTHON','JAVA'))

def menu_4():
    frase = input("Digite a frase. ")
    print(frase.lower())

def menu_5():
    separador_palavras = input("Bem vindo ao Separador de Str 'palavras.' ")
    print('palavras separadas : ' , separador_palavras.split())

def menu_6():
    palavras_user = input('Ordenador Alfabetico. ')
    contador_palavra = palavras_user.split()
    ordem_alfabetica = sorted(contador_palavra) 
    print(ordem_alfabetica)

user_numero_escolhido = int(input('digite um numero de 1 a 6. Para ter acesso aos Menus. '))

if user_numero_escolhido == 1:
    menu_1()
elif user_numero_escolhido == 2:
    menu_2()
elif user_numero_escolhido == 3:
    menu_3()
elif user_numero_escolhido == 4:
    menu_4()
elif user_numero_escolhido == 5:
    menu_5()
elif user_numero_escolhido == 6:
    menu_6()
else:
    print("Numero de 1 a 6. Porfavor \n :P  Bora sem enrrola!.")

##____________________________________________________________________________________________________________________________________________________________________
##EXERCICIO  9 : 

def removedor_vogais():
    
    frase = input('digite uma frase : ')
    return frase.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

print(removedor_vogais())

##____________________________________________________________________________________________________________________________________________________________________
##EXERCICIO  10 :
def contador_texto():
    texto = input("Digite o texto: no contador de caracters.")
    return f"A frase possui {len(texto)} caracters."

print(contador_texto())

##____________________________________________________________________________________________________________________________________________________________________
##DESAFIO:
