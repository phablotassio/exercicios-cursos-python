n=1
while n > 0:
    n=int(input('Digite um numero para calcular fatorial ou 0 para sair'.upper()))
    fatorial = 1
    n1 = n
    while n1 > 0:
        fatorial *= n1
        n1 -= True
    if n >= 0:
        print('O FATORIAL DE {} É {}'.format(n,fatorial))
    #n = int(input('Digite um numero para calcular fatorial ou 0 para sair'.upper()))