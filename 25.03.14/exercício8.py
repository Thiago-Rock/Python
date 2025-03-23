# Exemplo 8 - Faça um algoritmo que calcule as raízes da equação quadrática  
# ax²+bx+c = 0 , pressupondo que seu delta SEMPRE será positivo e sempre terá uma raiz exata.

print("Neste programa calcularemos as raízes de uma equação do segundo grau\n\n")

Coef_A = float(input("Digite o valor do coeficiente A: "))
Coef_B = float(input("Digite o valor do coeficiente B: "))
Coef_C = float(input("Digite o valor do coeficiente C: "))
Delta = pow(Coef_B,2) - 4*Coef_A*Coef_C
Raiz1 = (-Coef_B + pow(Delta,0.5))/(2*Coef_A)
Raiz2 = (-Coef_B - pow(Delta,0.5))/(2*Coef_A)
print("A equação possui duas raízes reais e diferentes:\n x_1 = ", Raiz1, " e x_2 = ", Raiz2)

