#Exemplo 9 - A Loja Mamão com Açúcar está vendendo seus produtos em até 4 
# (quatro) prestações sem juros. Faça um algoritmo que receba um valor de 
# uma compra e mostre o valor do preço com desconto a vista de 5% , 
# das prestações em 2 X , 3 X e 4 X .

Valor_produto = float(input("Entre com o valor do produt\n"))
Vista = Valor_produto*(1-0.05)
X_2 = Valor_produto/2
X_3 = Valor_produto/3
X_4 = Valor_produto/4
print("O valor à vista fica R$ {:.2f}".format(Vista))
print("\nDividindo em em duas parcelas fica R$ {:.2f}".format(X_2))
print("\nDividindo em três parcelas fica R$ {:.2f}".format(X_3))
print("\nDividindo em quatro parcelas fica R$ {:.2f}".format(X_4))