num_1 = int(input("Entre com o primeiro número: "))
num_2 = int(input("Entre com o segundo número: "))
num_3 = int(input("Entre com o terceiro número: "))

print("\nOs números em ordem crescente ficam:\n")
if num_1 < num_2 and num_1 < num_3:
    if num_2 < num_3:
        print(num_1,", ",num_2,", ",num_3)
    else:
        print(num_1,", ",num_3,", ",num_2)
elif num_2 < num_3:
    print(num_2,", ",num_3,", ",num_1)
else:
    print(num_3,", ",num_2,", ",num_1)

print("\n######################################################\n")

if num_1 < num_2:
    if num_2 < num_3:
        print(num_1,", ",num_2,", ",num_3)
    else:
        if num_1 < num_3:
            print(num_1,", ",num_3,", ",num_2)
        else:
            print(num_3,", ",num_1,", ",num_2)
else:
    if num_1 < num_3:
        print(num_2,", ",num_1,", ",num_3)
    else:
        if num_2 < num_3:
            print(num_2,", ",num_3,", ",num_1)
        else:
            print(num_3,", ",num_2,", ",num_1)  
  
