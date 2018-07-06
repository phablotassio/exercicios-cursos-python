festa = 'Progama'
print('='*20)
print('{:=^20}'.format(festa))
tconvidados = int(input('Quantas Pessoas Irao A festa'))
convidados = []
i = 1
while i<tconvidados:
    convidados.append(input('Digite o nome do convidado {}'.format(i)))
    i += 1
for u in convidados:
    print('{}'.format(u))
