n1 = int(input('Digite um numero inteiro: '))
impar = 0
i = 0
while impar < n1:
    if i % 2 != 0:
        impar += 1
        print(i)
    i += 1

