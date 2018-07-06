resp = int(input('Ola Seja Bem Vindo A tabela de Conversao\nDigite uma opcao para Continuar\n1 para converter de celsius para fire\n2 para converter de Fire para celsius\n3 para sair\n'))
if resp == 1:
    celsius = float(input('Digite a Temperatura em Celsius: '))
    fire = (1.8*celsius) + 32
    print('A temperatura em fire é {:.2f}'.format(fire))
elif resp == 2:
    fire = float(input('Digite a temperatura em Fahre: '))
    celsius = (fire-32)/1.8
    print('A temperatura em celsius é {:.2f}'.format(celsius))
elif resp == 3:
    print('Saindoo')
    exit()
else:
    print('Opcao invalida')
   
