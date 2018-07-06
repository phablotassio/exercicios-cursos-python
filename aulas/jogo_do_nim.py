computador_ganhou=0
eu_ganhei=0
def usuario_escolhe_jogada(n,m):
    resta=0
    pecas=int(input('Quantas peças você vai tirar?'))
    resta = n-pecas
    if  pecas > m or pecas <= 0 or pecas > n:
        while pecas > m or pecas <= 0 or pecas > n:
            print('Oops! Jogada inválida! Tente de novo.')
            pecas = int(input('Quantas peças você vai tirar?'))
    if pecas < 2:
        print('Você tirou uma peça.')
        if resta != 1:
            print('Agora restam {} peças no tabuleiro.'.format(resta))
        else:
            print('Agora resta apenas uma peça no tabuleiro.')
    else:
        print('Voce tirou {} peças.'.format(pecas))
        if resta != 1:
            print('Agora restam {} peças no tabuleiro.'.format(resta))
        else:
            print('Agora resta apenas uma peça no tabuleiro.')
    return pecas
def computador_escolhe_jogada(n,m):
    if m >= n:
        m=n
    else:
        sobrou = n % (m + 1)  # sobrou recebe o resto da divisão
        if sobrou > 0:  # Já que não é menor que m, e maior que 0 então...
            m = sobrou  # retorne o resto
    resta=n-m
    if m==1:
        print('O computador tirou uma peça.')
        if resta > 1:
            print('Agora restam {} peças no tabuleiro.'.format(resta))
        elif resta == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
    else:
        print('O computador tirou {} peças'.format(m))
        if resta > 1:
            print('Agora restam {} peças no tabuleiro.'.format(resta))
        elif resta == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
    return m
def partida ():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    j = n
    i = 1
    if m > n or m <=0 or n < m:
        print('Oops! Jogada inválida! Tente de novo.')
        while m > n or m<=0 or n < m:
            m = int(input('Limite de peças por jogada? '))
    if  n % (m + 1)==0:
        print('Voce começa!')
        n = n - (usuario_escolhe_jogada(n, m))
        #n=n-m
        while n >= 0:
            if i%2!=0:
                if m >= n:
                    print('Fim do jogo! O computador ganhou!')
                    global computador_ganhou
                    computador_ganhou += 1
                    break
                    #m = n
                else:
                    n=n-(computador_escolhe_jogada(n, m))
                    #n = n - m
                if n==0:
                    print('Fim do jogo! O computador ganhou!')
                    #global computador_ganhou
                    computador_ganhou += 1
                    break

            else:
                n = n - (usuario_escolhe_jogada(n, m))
                #n = n - m
                if n==0:
                    print('Fim do jogo! O Usuario ganhou!')
                    global eu_ganhei
                    eu_ganhei+=1
                    break
            i+=1

    else:
        print('Computador começa!')
        if m >= n:
            print('Fim do jogo! O computador ganhou!')
            computador_ganhou += 1
            exit()
        else:
            n = n - (computador_escolhe_jogada(n, m))
            #n = n - m
        while n >= 0:
            if i%2!=0:
                n = n - (usuario_escolhe_jogada(n, m))
                #n = n - m
                if n == 0:
                    print('Fim do jogo! O Usuario ganhou!')
                    eu_ganhei += 1
                    break
            else:
                if m > n:
                    m = n
                n = n - (computador_escolhe_jogada(n, m))
                #n = n - m
                if n == 0:
                    print('Fim do jogo! O computador ganhou!')
                    computador_ganhou += 1
                    break
            i+=1
def campeonato ():
    partida()
    partida()
    partida()
    print('Placar: Você {} X {} Computador'.format(eu_ganhei,computador_ganhou))

print('Bem-vindo ao jogo do NIM! Escolha:')
print('1 - para jogar uma partida isolada ')
print('2 - para jogar um campeonato 2')
print('3 para sair do jogo')
opcao=int(input())
if opcao == 1:
    partida()
elif opcao == 2:
    campeonato()
elif opcao == 3:
    print('Saindo do jogo')
else:
    while opcao > 3:
        print('Opcao Invalida')
        opcao=int(input())
