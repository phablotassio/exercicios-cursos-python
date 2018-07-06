import random
nome = 'phablo'
x=len(nome)
lista_mulheres = ['Anny','Carol','Mylena', 'Pollyana']
lista_mulheres.append(input('Digite um Nome Para Adicionar A lista'))
lista_mulheres.remove(input('Digite um nome Para remover da lista '))
lista_mulheres.clear()#LIMPA LISTA
print(lista_mulheres)
#print(random.choice(lista_mulheres))#sorteando esposa
print(nome[::-1])#invertendo nome