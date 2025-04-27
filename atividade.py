'''Questão 03 - Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua cerimônia de formatura. Construa um programa para cadastrar os nomes das pessoas que compraram a rifa.  Ao fim, o programa deve sortear o ganhador e imprimir o nome dele.
Para desenvolver esse programa, observe o exemplo a seguir de como fazer o sorteio em uma lista:
import random
lista = [1,2,3,4,5]
random.shuffle(lista)              #embaralha a lista
sorteado = random.choice(lista)    #sorteia aleatoriamente um elemento
print(sorteado)  
'''

rifa = []
resp = "s"
while True:
    if resp.upper() == "S":
        nome = input("Informe um nome: ")
        rifa.append(nome)
        resp = input("Gostaria de cadastrar mais um nome[S|N] ?")  
    else:
        break
print("Os participantes do sorteio são:")
print(rifa)
import random
random.shuffle(rifa)
sorteado = random.choice(rifa)
print("O ganhador foi: {}".format(sorteado))