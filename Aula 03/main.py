#Tendo como como dados de entrada a altura e peso de uma pessoa, construa um algoritimo que calcule seu IMC

peso = float (input("Digite o seu peso: " ))
altura = float(input("Digite o seu altura: " ))
IMC = ( peso/altura **2) 
print (f"O seu calculo IMC é: {IMC:.2f}") 


