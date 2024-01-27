#IMC

nome = input('Informe seu nome: ')
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / altura **2

print(f'{nome}, tem {altura:.2f}, de altura',)
print(f'seu peso é {peso} e seu imc é {imc:.2f}')