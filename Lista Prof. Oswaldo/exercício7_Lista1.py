'''7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. 
Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.  '''

dia = int(input("Qual o dia? "))
mes = int(input("Qual o mês? "))
dias_acumulados = 30*(mes - 1) + dia

print(f"Já se passaram {dias_acumulados} dias desde o início do ano")