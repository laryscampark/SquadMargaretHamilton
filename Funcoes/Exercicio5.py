def vogais(frase):
    return sum(1 for char in frase.lower() if char in "aeiou")

frase = input("Digite uma frase: ")

result = vogais(frase)
print(f"Total de vogais na frase: {result}")
