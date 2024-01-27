n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print(f'O primeiro número {n1} é maior que os números: {n2} e {n3}')
elif n2 >= n1 and n2 >= n3:
    print(f'O segundo número {n2} é maior que os números: {n1} e {n3}')
else:
    print(f'O terceiro número {n3} é maior que os números: {n1} e {n2}')