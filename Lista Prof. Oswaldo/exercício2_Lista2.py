'''2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” 
e estado civil seja “CASADA”, solicitar o tempo de casada (anos). '''

nome = input("Entre com o nome: ")
sexo = int(input("\nEntre com o sexo: \n1 - Para feminino \n2 - Para masculino: \n"))
estado_civil = int(input("\nEntre com o estdao cívil: \n1 - Para CASADO (A)\n2 - Para SOLTEIRO(A)"))

if (sexo == 1) and (estado_civil == 1):
    tempo = int(input("\nA quantos anos está casada? "))
