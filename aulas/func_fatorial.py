def fatorial (numero):
    fatorials = 1
    while numero > 0:
        fatorials *= numero
        numero -= 1
    print(fatorials)
fatorial (5)