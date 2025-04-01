temps = [[20, 19.5],[20, 19.7],[20, 20.2],[20,20.1],[21,19.9],[21,20.7],[21,21.2],[21,21.5],[25,25.5],[25,24.7],[25,25.2],[25,24.1]]
media_PV = 0
media_SP = 0
desvio_PV = 0
desvio_SP = 0
n = 0
''' PARTE 1: CALCULO DA MÉDIA'''
controle=0
for linha in temps:
    for PV in linha:
        if controle % 2 == 0:
            media_PV += PV
            controle+=1
            n+=1
            
            
        else:
            media_SP += PV
            controle+=1

media_PV = media_PV/n
media_SP = media_SP/n 
'''FIM PARTE1'''

'''PARTE 2: CALCULO DA VARIÂNCIA'''
controle=0
for linha in temps:
    for j in linha:
        if controle % 2 == 0:
            desvio_PV += pow(j - media_PV,2)
            controle+=1
            
            
            
        else:
            desvio_SP += pow(j - media_SP,2)
            controle+=1

desvio_PV = pow(desvio_PV/n,0.5)
desvio_SP = pow(desvio_SP/n,0.5)
'''FIM PARTE 2'''


print(media_PV)
print(media_SP)
print("n = ", n)
print(desvio_PV)
print(desvio_SP)
       
