import os
import json

dicionario_pessoas = {}
if os.path.exists("meu_dici.json"):
    with open("meu_dici.json", "r") as arquivo:
        dicionario_pessoas = json.load(arquivo)


def criar_arquivo():
    try:
        if os.path.exists("meu_dici.json"):
            print("\nAviso - O arquivo já existe!")
            return
        else:
            with open("meu_dici.json", 'w') as arquivo:
                json.dump(dicionario_pessoas, arquivo)
        print("arquivo 'meu_dici.json' criado com sucesso")
    except Exception as e:
        print(f'ERRO {e}')


def ler_arquivo():
    try:
        with open("meu_dici.json", "r") as arquivo:
            conteudo = json.load(arquivo)
        for pessoa, idade, email in conteudo.items():
            print(f"\nÚsuario: {pessoa}, idade: {idade}, Email: {email} ")
    except Exception as e:
        print(f'ERRO {e}')


def adicionar_nome():
    pessoa = input("\nDigite um nome para adicionar: ")
    idade = input("\nDigite sua idade para adicionar: ")
    email = input("\nDigite o seu email para adicionar: ")
    arquivo = open("meu_dici.json", "w", encoding="utf-8")
    dicionario_pessoas[pessoa] = idade, email
    json.dump(dicionario_pessoas, arquivo)
    arquivo.close()
    print(f"[Sucesso] '{pessoa}' foi adicionado ao arquivo!")
    print(f"[Sucesso] '{idade}' foi adicionado ao arquivo!")
    print(f"[Sucesso] '{email}' foi adicionado ao arquivo!")
    

opcao = ""
while opcao != "0":
    print("\n======= MENU DO ARQUIVO =======")
    print("1. Criar arquivo inicial")
    print("2. Ler conteúdo do arquivo")
    print("3. Adicionar o seu nome, idade e email ao final")
    print("0. Sair do programa")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        criar_arquivo()
    elif opcao == "2":
        ler_arquivo()
    elif opcao == "3":
        adicionar_nome()
    elif opcao == "0":
        print("\nSaindo do sistema...")
    else:
        print("\nOpção Inválida - Escolha um número do menu.")
