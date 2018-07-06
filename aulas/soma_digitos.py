n1 = int(input('Digite um numero: '))
x=len(str(n1))
i=0
soma = n1 % 10
while i < x:
    if i >= 1:
        n1 = n1 // 10
        soma += n1 %10
    i+=1
print(soma)
