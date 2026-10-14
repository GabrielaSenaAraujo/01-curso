
# def criar_arquivo():
#     arquivo = open('atv1','w', encoding='utf-8')
#     arquivo.close

# def ler_arquivo():
#     arquivo = open('atv1', 'r', encoding='utf-8')
#     texto = arquivo.read()
#     print(texto)
#     arquivo.close


# def append_arquivo():
#     arquivo = open('atv1','a', encoding='utf-8')
#     arquivo.write(input('Digite a sua messagem: '))
#     arquivo.close



# criar_arquivo()
# append_arquivo()
# ler_arquivo()



def ler_texto():
    arquivo = open('texto_simples.txt', 'w', encoding='utf-8')
    arquivo.close

def ler_arquivo():
    arquivo = open('texto_simples.txt', 'r', encoding='utf-8')
    texto = arquivo.read()
    print(texto)
    arquivo.close


def append_texto():
    arquivo = open('texto_simples.txt', 'a', encoding='utf-8')
    arquivo = arquivo.write()    
    arquivo.close

          