pares = 0
impares = 0

while True:
    try:
        numero = int(input("Informe um número (ou 0 para encerrar): "))
        
        if numero == 0:
            break  
        
        if numero < 0:
            print("Por favor, informe apenas números positivos.")
            continue  
        
        pares += numero % 2 == 0
        impares += numero % 2 != 0

    except ValueError:
        print("Por favor, informe um número válido.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
