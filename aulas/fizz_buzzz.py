numero = int(input('Entre com um numero'))
if numero % 3 == 0 and numero % 5 == 0:
    print('FizzBuzz')
else:
    print('{}'.format(numero))