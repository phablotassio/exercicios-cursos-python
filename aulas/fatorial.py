numero = int(input('Digite um numero'))
i = 0
fatorial = 1
while i < numero:
    fatorial *= (i+1)
    i+=1
print(fatorial)