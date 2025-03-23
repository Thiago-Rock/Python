# Exercício 4 - Em épocas de pouco dinheiro, os comerciantes estão
# procurando aumentar suas vendas oferecendo descontos. Faça um
#valgoritmo que possa receber um valor de um produto e que escreva o novo
# valor tendo em vista que o desconto foi de 9%.

ValorProduto = float(input("Digite o valor do produto: "))
TaxaDesconto = 9
ValorProdutoFinal = ValorProduto*(1 - TaxaDesconto/100)
print("\nO valor do produto com desconto é de: R$ {:.2f}".format(ValorProdutoFinal))