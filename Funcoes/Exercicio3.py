def celsius_Fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_Celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha a opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

op = input('Deseja a opção que deseja: ')

if op == "1":
    temperatura_C = float(input("Digite a temperatura em graus Celsius: "))
    result = celsius_Fahrenheit(temperatura_C)
    print(f"A temperatura em Fahrenheit é: {result:.2f}°F")
elif op == "2":
    temperatura_F = float(input("Digite a temperatura em graus Fahrenheit: "))
    result = fahrenheit_Celsius(temperatura_F)
    print(f"A temperatura em Celsius é: {result:.2f}°C")
else:
    print("Opção inválida. Por favor, escolha 'C-F' ou 'F-C'.")