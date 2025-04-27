'''Questão 05 - Crie um programa que leia um valor N, tal que N>1. O programa deve gerar, aleatoriamente, uma lista L. Por fim, o programa deve calcular e imprimir a média geométrica dos N elementos da lista.
Para desenvolver esse programa, observe o exemplo a seguir de como gerar uma lista com valores aleatórios no intervalo [1,10]:

from random import randrange
import random
#Gera uma lista contendo 5 elementos. Os elementos estão no intervalo [1,10]
L = [randrange(1,11) for i in range(5)]
print(L)
 
'''


N = int(input("Informe um valor inteiro maior que 1: "))
sorteados = []
soma = 0
if N > 1:
    import random
    L = [random.randrange(1,N) for i in range(3)]
    print(L)
else:
    print("O valor digitado é menor ou igual a zero, NÃO PODE!!")
media = sum(L)/len(L)
print("A média dos valores sorteados é {}".format(media))