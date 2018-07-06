valor = float(input('Digite o valor do produto'))
vdesc = float(valor-(valor*0.05))
print('{:.2f} reais com 5% de desconto fica {:.2f}'.format(valor,vdesc))