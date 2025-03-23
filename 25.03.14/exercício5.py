#Exercício 5 - Faça o algoritmo que calcule o valor em Reais, correspondente aos 
# dólares que um turista possui para trocar para reais. O algoritmo deve solicitar os seguintes dados: 
# Quantidade de dólares que deseja trocar : 
# Qual a cotação do dólar?

ValorDolar = float(input("Quantidade de dólares que deseja trocar : "))
CotacaoDolar = float(input("\nQual a cotação do dólar: "))
ValorReal = ValorDolar*CotacaoDolar
print("\nVocê receberá R$", ValorReal, "em reais.")