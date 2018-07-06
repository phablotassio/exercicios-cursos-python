def eprimo(numero):
    i=0
    conta = 0
    while i<numero:
        if i >= 1 and numero % i == 0:
            conta += 1
        i += 1
    if conta == 1:
        return True
    else:
        return False
n = int(input('Digite um numero inteiro :'))
if n == 0:
    print('Saindo do progama'.upper())
while n > 0:
    if eprimo(n):
        print('{} é primo.'.format(n))
    else:
        print('{} não é primo'.format(n))
    n = int(input('Digite um numero inteiro :'))
    if n == 0:
        print('Saindo do progama'.upper())