num_1 = float(input("Entre com o número 1: "))
num_2 = float(input("Entre com o número 2: "))
num_3 = float(input("Entre com o número 3: "))

'''
if num_1 > num_2:
    if num_1 > num_3:
        print("O primeiro é o maior de todos")
    else:
        print("O terceiro é o maior de todos")
else:
    if num_2 > num_3:
        print("O segundo é o maior de todos")
    else:
        print("O terceiro é o maior de todos")
'''
if num_1 > num_2 and num_1 > num_3:
    print("O peimeiro é o maior de todos")
elif num_2 > num_3:
    print("O segundo é o maior de todos")
else:
    print("O terceiro é o maior de todos") 