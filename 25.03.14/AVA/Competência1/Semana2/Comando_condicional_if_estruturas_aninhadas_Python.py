temp = float(input('Qual a temperatura? '))
if temp < 7:
    print("Congelando!")
elif temp < 10:
    print("Frio!")
elif temp < 26:
    print("Ótimo!")
else:
    print("Muito quente!")