n1 = int(input('Digite um numero: '))
soma = 0
i = 0
while i < n1:
    if i >= 1 and n1 % i == 0:
        soma += 1
    i += 1
if soma == 1:
    print('primo')
else:
    print('não primo')