#ERP app

import tkinter as tk
from tkinter import messagebox
import pesquisar_produto

def abrir_janela(mensagem):
    nova_janela = tk.Toplevel()
    nova_janela.title("Ação qualquer...")

    label = tk.Label(nova_janela, text=mensagem, padx=20, pady=20)
    label.pack()

    botao_fechar = tk.Button(nova_janela, text="Sair", command=nova_janela.destroy)
    botao_fechar.pack(padx=20, pady=10)

#Funções para as diferentes funcionalidades do sistema ERP

def pesquisar_produto():
    abrir_janela("Pesquisar produto")

def checar_estoque():
    abrir_janela("Checar estoque")

def acrescentar_estoque():
    abrir_janela("Acrescentar ao estoque")

def remover_estoque():
    abrir_janela("Remover do estoque")

def cadastrar_produto():
    abrir_janela("Cadastrar produto")

# Criar a janela principal 
janela_principal = tk.Tk()
janela_principal.title("Sistema ERP IESGO")
janela_principal.attributes('-fullscreen', True)

# Configurar icones do menu 
icon_pesquisar = tk.PhotoImage(file="procurar.png")
icon_estoque = tk.PhotoImage(file="estoque.png")
icon_acrescentar = tk.PhotoImage(file="acrescentar.png")
icon_remover = tk.PhotoImage(file="remove.png")
icon_cadastrar = tk.PhotoImage(file="cadastrar.png")

#Criar botões com icones
botao_pesquisar = tk.Button(janela_principal, image=icon_pesquisar, command=pesquisar_produto)
botao_estoque = tk.Button(janela_principal, image=icon_estoque,command=checar_estoque)
botao_acrescentar = tk.Button(janela_principal, image=icon_acrescentar,command=acrescentar_estoque)
botao_remover = tk.Button(janela_principal, image=icon_remover,command=remover_estoque)
botao_cadastrar = tk.Button(janela_principal, image=icon_cadastrar,command=cadastrar_produto)

#Exibir os botões na janela
botao_pesquisar.pack()
botao_estoque.pack()
botao_acrescentar.pack()
botao_remover.pack()
botao_cadastrar.pack()

#Looping janela principal
janela_principal.mainloop()
