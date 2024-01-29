def converter(valor, taxa):
    return valor / taxa

valores = float(input("Informe a quantidade de dinheiro em reais: R$"))

conversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

print("Quantidade que poderia comprar em cada moeda estrangeira:")
for moeda, taxa in conversao.items():
    print(f"{moeda}: ${converter(valores, taxa):.2f}")
