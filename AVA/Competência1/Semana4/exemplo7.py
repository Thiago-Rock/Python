opcao = "S"
while opcao != "N":
    a = float(input("Entre com o primeiro valor: "))
    b = float(input("Entre com o segundo valor: "))
    print(a+b)
    opcao = input("Deseja continuar?\nDigite S para sim e N para não ")
else:
    print("Tchau!!!") 