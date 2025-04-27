'''Questão 02 - Os professores de educação física estão organizando uma seletiva para montar a equipe de natação. Para isso, eles convocaram os 7 melhores tempos da última competição e marcaram o tempo de cada um dos nadadores, na prova dos 25 metros, estilo nado livre.
Considerando que não houveram tempos iguais, construa um programa que leia o nome e o tempo(em segundos) de cada atleta e, em seguida, gere o seguinte relatório:
a) Nadador com o melhor desempenho:
b) Nadador com o pior desempenho:
c) Tempo médio dos nadadores:
Dica: Crie duas listas: uma para cadastrar os nomes dos nadadores e outra para guardar os seus respectivos tempos.

'''

nadadores = []
tempos = []
resp = "S"
soma_tempos = 0
count = 0

while True:
    if resp.upper() == "S":
        nome = input("Informe o NOME do nadador: ")
        nadadores.append(nome)
        time = int(input("Informe o TEMPO marcado: "))
        soma_tempos +=time
        count += 1
        tempos.append(time)
        resp = input("Incluir dados de outro NADADOR: [S|N]: ")
    else:
        break    
menor_tempo = tempos.index(min(tempos))
print(nadadores)
print(tempos)
melhor_nadador = nadadores[menor_tempo]
melhor_tempo = tempos[menor_tempo]
maior_tempo = tempos.index(max(tempos))
pior_nadador = nadadores[maior_tempo]
pior_tempo = tempos[maior_tempo]
print("Nadador com melhor desempenho: {}, com o tempo de {} segundos".format(melhor_nadador,melhor_tempo))
print("Nadador com o pior desempenho: {}, com o tempo de {} segundos".format(pior_nadador,pior_tempo))
media_tempos = soma_tempos/count
print("A média dos tempos dos nadadores é de: {} segundos".format(media_tempos))
