'''10. Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano. 
Cada ponto é um par ordenado (x,y). '''
import os
print("Entre com as coodenadas do primeiro ponto\n")
x_1 = float(input("Forneça a coordenada x: "))
y_1 = float(input("Forneça a coordenada y: "))
os.system("cls")

print("Entre com as coodenadas do Segundo ponto\n")
x_2 = float(input("Forneça a coordenada x: "))
y_2 = float(input("Forneça a coordenada y: "))
os.system("cls")

distancia = pow((x_1 - x_2)**2 + (y_1 - y_2)**2,0.5)

print("A distância ente o ponto (",x_1,", ",y_1,") e o ponto (",x_2,", ",y_2,") é de : ",distancia, "unidades")