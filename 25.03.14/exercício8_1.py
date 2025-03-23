print("Neste programa calcularemos as raízes de uma equação do segundo grau\n\n")

Coef_A = float(input("Digite o valor do coeficiente A: "))

if Coef_A == 0:
    while Coef_A == 0:
        print("\nO coeficiente A não pode ser igual a 0. Digite novamente.")
        Coef_A = float(input("Digite o valor do coeficiente A: "))

Coef_B = float(input("Digite o valor do coeficiente B: "))
Coef_C = float(input("Digite o valor do coeficiente C: "))
Delta = pow(Coef_B,2) - 4*Coef_A*Coef_C
if Delta < 0:
    print("A equação não possui raízes reais.")
elif Delta == 0:
    Raiz = -Coef_B/(2*Coef_A)
    print("A equação possui duas raizes reais e iguais:\n x_1 = x_2 = ", Raiz)
else:
    Raiz1 = (-Coef_B + pow(Delta,0.5))/(2*Coef_A)
    Raiz2 = (-Coef_B - pow(Delta,0.5))/(2*Coef_A)
    print("A equação possui duas raízes reais e diferentes:\n x_1 = ", Raiz1, " e x_2 = ", Raiz2)