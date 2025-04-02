num_1 = float(input("Entre com o primeiro número: "))
num_2 = float(input("Entre com o segundo número: "))
num_3 = float(input("Entre com o terceiro número: "))

if num_1 > num_2:
    soma = num_1
    if num_2 > num_3:
        soma += num_2
    else:
        soma += num_3
else:
    soma = num_2
    if num_1 > num_3:
        soma += num_1
    else:
        soma += num_3

print("A soma foi: ", soma)