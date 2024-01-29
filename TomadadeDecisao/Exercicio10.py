
n1 = int(input("Informe o primeiro número inteiro: "))
n2 = int(input("Informe o segundo número inteiro: "))
n3 = int(input("Informe o terceiro número inteiro: "))

if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1

print(f"Números em ordem crescente: {n1}, {n2}, {n3}")
