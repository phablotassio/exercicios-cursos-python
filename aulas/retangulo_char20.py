largura = int(input('Digite a largura:'))
altura = int(input('Digite a altura:'))
i=1
while i <= altura:
    j = 1
    if i==1 or i == altura:
        while j <= largura:
            print('#',end='')
            j += 1
    else:
        while j <= largura:
            if j== 1 or j == largura:
                print('#',end='')
            else:
                print(' ',end='')
            j+=1
    print('')
    i += 1