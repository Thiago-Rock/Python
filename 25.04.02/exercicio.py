'''Este exercício consiste em receber três medidas verificar, pela condição 
de existência do triângulo, se pode ou não formar um triângulo. Em seguida
classifica o triângulo em EQULÁTERO, ESCALENO OU ISÓSCELES'''


A = float(input("Entre com o primeiro lado do trângulo: "))
B = float(input("Entre com o segundo lado do trângulo: "))
C = float(input("Entre com o terceiro lado do trângulo: "))

print("#######################################################")
if (A + B) > C and (A + C) > B and (B + C) > A:
    print("Pode formar um triângulo!!!")
    if A == B and A == C and B == C:
        print("\nEste é um triângulo EQUILÁTERO")
    elif A != B and A != C and B != C:
        print("\nEste é um triângulo ESCALENO")
    else:
        print("\nEste é um triângulo ISÓSCELES")
else:
    print("Não forma um triângulo!!!")
