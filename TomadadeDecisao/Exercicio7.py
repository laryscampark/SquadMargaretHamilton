idade= int(input('Informe sua idade: '))

if idade <= 18:
    if idade <= 12:
        print('É uma criança')
    else:
        print('É um adolescente')
    
elif idade < 65:
    print('É um adulto')
else:
    print('É um idoso')