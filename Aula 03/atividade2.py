valor_hora = float(input("Qual valor por hora?"))
hora_trabalhada = float (input("Quanto horas trabalhadas?"))

salario_bruto = hora_trabalhada * valor_hora

inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
ir = salario_bruto * 0.11
salario_liquido = salario_bruto - ir - inss - sindicato
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Imposto de renda (11%): R$ {ir:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")


