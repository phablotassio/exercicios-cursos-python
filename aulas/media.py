n1 = float (input('Digite sua nota 1'))
n2 = float (input('Digite sua nota 2'))
media = (n1+n2)/2
if media < 5:
    print('voce foi reprovado com media {:.3f}'.format(media))
elif media >= 5 and media <6:
    print('voce esta de recuperacao com media{:.3f}'.format(media))
else:
    print('voce foi Aprovado com media {:.3f}'.format(media))
