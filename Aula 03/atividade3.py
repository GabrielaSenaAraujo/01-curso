print ("-"*30)
print("FATURAMENTO PIZZARIA")
print("-"*30)

valor_pizza = float(input("Valor pizza? "))
pizzas_vendidas = float(input("Pizza vendidas? "))
faturamento_bruto = valor_pizza * pizzas_vendidas
custos_fixos = faturamento_bruto * 0.3
custo_variavel = faturamento_bruto * 0.2
faturamento_liquido = faturamento_bruto - custos_fixos - custo_variavel
print(f"Faturamento bruto: R$ {faturamento_bruto:.2f}")
print(f"Faturamento líquido: R$ {faturamento_liquido:.2f}")
