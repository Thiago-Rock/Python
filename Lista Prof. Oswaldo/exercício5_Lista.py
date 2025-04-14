'''5. Um motorista deseja colocar no seu tanque X reais de gasolina. 
Escreva um algoritmo para ler o preço do litro da gasolina e o valor
do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.'''

preco_gasolina = float(input("Informe o preço da gasolina"))
dinheiro = float(input("Quantos reais você deseja colocar de gasolina?"))

litros = dinheiro/preco_gasolina

print(f"Com R$ {dinheiro}"+" você consegue colocar {:.2f}".format(litros))