print('-'*40)
print('--------- SISTEMA VOTAÇÃO ------------')
print('-'*40)
nome = (input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))

if idade < 16 : 
 print(f'{nome}, você não pode votar =(')
elif idade < 18 :
  print(f'{nome}, você pode votar se quiser')
elif idade < 70:
  print(f'{nome}, eres obrigado(a) =)')
else:
  print (f'{nome}, você pode votar se quiser)')