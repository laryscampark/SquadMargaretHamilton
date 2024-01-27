mediaTotal = []

for i in range(5):
    notas = [float(input(f'Informe a nota {j + 1} do aluno {i + 1}: ')) for j in range(4)]
    media = sum(notas)/4
    mediaTotal.append(media)   
aprovados = sum(1 for media in mediaTotal if media >= 7)

print(f'O número de alunos com média maior ou igual a 7 foram : {aprovados}')

