computador_ganhou=0
eu_ganhei=0
def usuario_escolhe_jogada(n,m):
    resta=0
    pecas=int(input('Quantas peças você vai tirar?'.upper()))
    resta = n-pecas
    if  pecas > m or pecas <= 0 or pecas > n:
        while pecas > m or pecas <= 0 or pecas > n:
            print('Oops! Jogada inválida! Tente de novo.'.upper())
            pecas = int(input('Quantas peças você vai tirar?'.upper()))
    if pecas < 2:
        print('Você tirou uma peça.'.upper())
        if resta != 1:
            print('Agora restam {} peças no tabuleiro.'.upper().format(resta))
        else:
            print('Agora resta apenas uma peça no tabuleiro.'.upper())
    else:
        print('Voce tirou {} peças.'.upper().format(pecas))
        if resta != 1:
            print('Agora restam {} peças no tabuleiro.'.upper().format(resta))
        else:
            print('Agora resta apenas uma peça no tabuleiro.'.upper())
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
        print('O computador tirou uma peça.'.upper())
        if resta > 1:
            print('Agora restam {} peças no tabuleiro.'.upper().format(resta))
        elif resta == 1:
            print('Agora resta apenas uma peça no tabuleiro.'.upper())
    else:
        print('O computador tirou {} peças'.upper().format(m))
        if resta > 1:
            print('Agora restam {} peças no tabuleiro.'.upper().format(resta))
        elif resta == 1:
            print('Agora resta apenas uma peça no tabuleiro.'.upper())
    return m
def partida ():
    jogo_acabou = True
    n = int(input('Quantas peças? '.upper()))
    m = int(input('Limite de peças por jogada? '.upper()))
    j = n
    i = 1
    if m > n or m <=0 or n < m:
        print('Oops! Jogada inválida! Tente de novo.'.upper())
        while m > n or m<=0 or n < m:
            m = int(input('Limite de peças por jogada? '.upper()))
    if  n % (m + 1)==0:
        print('Voce começa!'.upper())
        n = n - (usuario_escolhe_jogada(n, m))
        #n=n-m
        while n >= 0:
            if i%2!=0:
                if m >= n:
                    print('Fim do jogo! O computador ganhou!'.upper())
                    global computador_ganhou
                    computador_ganhou += 1
                    break
                    #m = n
                else:
                    n=n-(computador_escolhe_jogada(n, m))
                    #n = n - m
                if n==0:
                    print('Fim do jogo! O computador ganhou!'.upper())
                    #global computador_ganhou
                    computador_ganhou += 1
                    break

            else:
                n = n - (usuario_escolhe_jogada(n, m))
                #n = n - m
                if n==0:
                    print('Fim do jogo! O Usuario ganhou!'.upper())
                    global eu_ganhei
                    eu_ganhei+=1
                    break
            i+=1

    else:
        print('Computador começa!'.upper())
        if m >= n:
            print('Fim do jogo! O computador ganhou!'.upper())
            computador_ganhou += 1
            jogo_acabou=False
        else:
            n = n - (computador_escolhe_jogada(n, m))
            #n = n - m
        while n >= 0 and jogo_acabou:
            if i%2!=0:
                n = n - (usuario_escolhe_jogada(n, m))
                #n = n - m
                if n == 0:
                    print('Fim do jogo! O Usuario ganhou!'.upper())
                    eu_ganhei += 1
                    break
            else:
                if m > n:
                    m = n
                n = n - (computador_escolhe_jogada(n, m))
                #n = n - m
                if n == 0:
                    print('Fim do jogo! O computador ganhou!'.upper())
                    computador_ganhou += 1
                    break
            i+=1
def campeonato ():
    print('**** RODADA 1 ****')
    partida()
    print('**** RODADA 2 ****')
    partida()
    print('**** RODADA 3 ****')
    partida()
    print('PLACAR: VOCÊ {} X {} COMPUTADOR'.format(eu_ganhei,computador_ganhou))
def jogo ():
    print('='*50)
    print('Bem-vindo ao jogo do NIM! Escolha:'.upper())
    print('1 - para jogar uma partida isolada '.upper())
    print('2 - para jogar um campeonato '.upper())
    print('3 - Como jogar '.upper())
    print('4 - para sair do jogo'.upper())
    print('='*50)
    opcao=int(input())
    if opcao == 1:
        print('Voce escolheu uma Partida!'.upper())
        partida()
    elif opcao == 2:
        print('Voce escolheu um campeonato!'.upper())
        campeonato()
    elif opcao == 3:
        regras=' REGRAS '
        print('=' * 50)
        print('objetivo do jogo'.upper())
        print('tirar a ultima peça do tabuleiro'.upper())
        print('{:=^70}'.format(regras))
        print('nao e possivel tirar mais pecas que as que estao no tabuleiro '.upper())
        print('nao e possivel tirar mais pecas que o limite determinado no inicio do jogo'.upper())
        nim=input('digite NIM para voltar ao menu do jogo: '.upper())
        print(nim)
        if nim != 'NIM' and nim != 'nim':
            while nim != 'NIM' and nim != 'nim':
                nim = input('OPCAO INVALIDA! ')
        jogo()
    elif opcao == 4:
        print('Saindo do jogo'.upper())
    else:
        while opcao > 4:
            print('Opcao Invalida'.upper())
            opcao=int(input())
jogo()