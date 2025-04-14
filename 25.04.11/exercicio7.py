import os
opcao = "c"
while (opcao != 's' and opcao != 'S'):
    a = float(input("Entre com o primeiro valor: "))
    b = float(input("Entre com o segundo valor: "))
    soma = a + b
    print('A soma dos números é: ', soma)
    print('\n')
    print('Deseja continuar?\n')
    opcao = input('Degite s para sair ou c para continuar: ')
    os.system('cls')
    if opcao == 's' or opcao == 'S':
        os.system('cls')
        print('Obrigado por usar nosso serviço. Adeus!')
        break
    elif opcao != 'c' or opcao !='C':
        while opcao != 'c' and opcao != 'C':
            opcao = input("É (C) de CONTINUAR o retardado!!!\n")
            os.system('cls')

    else:
        continue

       

    
