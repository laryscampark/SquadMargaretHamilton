while True:
    nota = int(input('Informe uma nota de 0 a 10: '))
    
    if nota >=7:
        print(f'Sua nota foi {nota} você está aprovado')
        break
    else:
        print(f'Sua nota foi {nota} você está reprovado')