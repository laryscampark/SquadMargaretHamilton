horas = int(input('Informe o número de horas de exercicio físico por semana: '))

minutos = horas * 60
caloria = 5
caloria_semana = minutos * caloria
media =  caloria_semana * 4

print(f'Foi queimados total de {media:.2f} calor em um mês')