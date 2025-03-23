#A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. 
# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, 
# o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), 
# e quanto deve guardar numa conta de poupança (10% do total arrecadado). 
# Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, 
# faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular 
# os dados solicitados. 
print("Programa de calculo de faturamento")
print("##################################")
print("\n")

qtd_pao = int(input("Quantos pães foram vendidos : "))
qtd_broa = int(input("Quantas broas foram vendidas : "))

faturamento_dia = qtd_pao*0.12 + qtd_broa*1.5
guardar = faturamento_dia*0.1

print("O faturamento do dia foi de R$ {:.2f}".format(faturamento_dia))
print("O valor que deve guardar na poupança é de R$ {:.2f}".format(guardar))