n=1
lista = []
while n != 0:
    lista.append(int(input('Digite um numero para Adicionar a lista ou 0 para imprimir e sair')))
    if 0 in lista:
        n=0
lista.remove(0)
lista2=lista[::-1]
for x in lista2:
    print(x)