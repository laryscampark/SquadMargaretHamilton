t1 = int(input('Informe o primeiro lado do triangulo: '))
t2 = int(input('Informe o segundo lado do triangulo: '))
t3 = int(input('Informe o terceiro lado do triangulo: '))

if t1 == t2 == t3:
    print('É um equilátero pois todos os lados possuem o mesmo valor')
elif t1 == t2:
    print('É um isósceles pois possue dois lados com o mesmo valor')
else:
    print('É um escaleno pois todos os lados estão com medidas distintas')