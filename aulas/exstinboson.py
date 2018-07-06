#Crie um progama que retorne os 3 primeiros caractres de uma string
pal = input('Digite uma Palavra')
tletras = len(pal)
tres = pal[:3]
print('{} possui {} letras e as suas 3 primeiras letras sao {}'.format(pal,tletras,tres))