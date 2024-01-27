nome = input('Informe seu nome: ')
turno = input('Informe o turno que estuda: ')

if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Vespertino')
elif turno == 'N':
    print('Boa noite')
else:
    print('Valor inválido')