# Escreva um programa que calcule o salário líquido. Lembrando de
# declarar o salário bruto e o percentual de desconto do Imposto de
# Renda.
    # ● Renda até R$ 1.903,98: isento de imposto de renda;
    # ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
    # ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
    # ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
    # ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
#salario_bruto*(7.5/100)

nome = input('Informe seu nome: ')
salario = float(input('Informe seu salário: '))

if salario <= 1903.98 :
    print(f'O salário foi de {salario} e está insento de pagar imposto de renda')
elif 1909.99 <= salario >= 2886.65:
    desc = salario * 0.075
elif 2826.66 <= salario >=3751.05:
    desc = salario * 0.15
elif 3751.06 <= salario >= 4664.68:
    desc = salario * 0.225
else: 
    desc = salario * 0.275
    
result = salario - desc 

print(f'O salário bruto: $ {salario:.2f}')
print(f'Desconto do imposto de renda: R$ {desc:.2f}')
print(f'Salário liquido: R$ {result:.2f}')