def eprimo(numero):
    i=0
    conta = 0
    while i<numero:
        if i >= 1 and numero % i == 0:
            conta += 1
        i += 1
    if conta == 1:
        return 1
    else:
        return 0
def maior_primo (numero):
    i = 0
    primo = 0
    while i<=numero:
        if eprimo(i) == 1:
            primo=i
        i+=1
    return primo
