while:
    nota = float(input('Informe uma nota: '))
    
    if 0 <= nota >=10:
        print(f'A nota {nota} é um valor válido')
        break
    else:
        print(f'A nota {nota} é um valor inválido')