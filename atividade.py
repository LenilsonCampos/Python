'''Questão 01 - Um professor de matemática deseja construir um programa para gerar uma progressão aritmética (PA).
Para isso, devem ser informados 3 parâmetros de entrada:
a) Primeiro termo da PA
b) Quantidade de termos da PA
c) Razão dessa PA
Construa um programa para carregar e imprimir uma lista contendo os termos da PA, bem como a soma dos elementos da PA.
'''
termos_PA = []
a1 = int(input("Informe o 1º termo da PA: "))
termos_PA.append(a1)
termo = a1
an = int(input("Informe a quantidade de termos que terá essa PA: "))
razao = int(input("Informe a razão dessa PA: "))
for i in range(1,an):
    termo +=razao
    termos_PA.append(termo)
print(termos_PA)    
PA = a1 + ((an - 1)*razao)
print("O {}º termo dessa PA é: {}".format(an,PA)) 

    