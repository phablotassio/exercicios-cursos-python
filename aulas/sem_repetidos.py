def remove_repetidos(lista):
    lista2 = []
    x=len(lista)
    i=0
    while i < x:
        if lista [i] in lista [0:i]:
            print('',end='')
        else:
            lista2.append(lista[i])
        i+=1
    lista2.sort()
    return lista2
