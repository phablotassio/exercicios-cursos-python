segundos = int(input('Digite o total de Segundos'))

dias = segundos // 86400
horas = (segundos // 3600)%24
segundos_res = segundos % 3600
minutos = segundos_res // 60
seg_final = segundos_res % 60

print ('{} dias, {} horas, {} minutos, {} segundos'.format(dias,horas,minutos,seg_final))