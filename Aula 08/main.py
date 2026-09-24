# print("-"*25)
# for i in range (51):
#      print(i)
# print("-"*25)
# ##########################
# print("-"*25)
# for i in range (0,51,2):
#       print(i)
# print("-"*25)
# ##############################
   
# for i in range (50,0,-2):
#       print(i)
    
#Faça um programa que receba dois números inteiros e print os números inteiros ques estão no intervalo entre eles (inclusive eles)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
step = int(input('Quantos steps: '))

for i in range (n1, n2+1, step):
    print(i)
