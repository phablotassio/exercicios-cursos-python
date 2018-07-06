def maximo(n1,n2,n3):
    if n1 > n2 > n3:
        return n1
    elif n2 > n1 > n3:
        return n2
    elif n3 > n2 >n1 :
        return n3
    else :
        return n1