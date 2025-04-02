import re

email = input("Digite seu e-mail: ")
telefone = input("Digete seu telefone: ")
padrao_email = r'^[a-z 0-9]+@[a-z 0-9]+\.[a-z]{2,3}$' 
padrao_telefone = r'^\([0-9]{3}+\)+ +[0-9]{4,5}+\-[0-9]{4}$'

if re.match(padrao_email, email):
    print("e-mail válido")
else:
    print("e-mail inválido")

if re.match(padrao_telefone, telefone):
    print("telefone válido")
else:
    print("telefone inválido")
