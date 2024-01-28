def reverso(numero):
    n_invertido = int(str(numero)[::-1])
    return n_invertido

n = int(input('Digite um número inteiro: '))

result = reverso(n)
print(f'O reverso do número {n} é: {result}')