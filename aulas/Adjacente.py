n1 = int(input("Digite um número: "))
n2 = str(n1)
x = len (n2)
conta = 0
i = 0
while i < x-1:
    if n2[i] == n2 [i+1] and n2[i] in n2:
        conta += 1
    i += 1
if conta >=1:
    print('sim')
else:
    print('não')