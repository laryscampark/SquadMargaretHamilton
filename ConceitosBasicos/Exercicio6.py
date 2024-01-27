viagem = float(input('Informe a distancia da viagem: '))

aviao = 600
carro = 100
onibus = 80


viagem_aviao = aviao / viagem
viagem_carro = carro / viagem
viagem_onibus =  onibus / viagem

print(f'Tempo gasto de viagem de avião foi de {viagem_aviao:.2f} horas')
print(f'Tempo gasto de viagem de carro foi de {viagem_carro:.2f} horas')
print(f'Tempo gasto de viagem de onibus foi de {viagem_onibus:.2f} horas')