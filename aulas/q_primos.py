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
def n_primos(numeros):
    i=0
    primo = 0
    while i < numeros:
        if eprimo(i):
            primo += 1
        i+=1
    return primo
print(n_primos(11))