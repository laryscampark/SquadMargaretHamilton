
carrinho_compra = {}


def adiciona(carrinho, produto, quantidade, preco_unitario):
    if produto in carrinho:
        carrinho[produto]['quantidade'] += quantidade
    else:
        carrinho[produto] = {'quantidade': quantidade, 'preco_unitario': preco_unitario}


adiciona(carrinho_compra, 'Produto1', 2, 10.0)
adiciona(carrinho_compra, 'Produto2', 1, 20.0)
adiciona(carrinho_compra, 'Produto3', 3, 15.0)


def total_Carrinho(carrinho):
    total = 0.0
    for produto, info in carrinho.items():
        total += info['quantidade'] * info['preco_unitario']
    return total


total_carrinho = total_Carrinho(carrinho_compra)


print("Carrinho de Compras:")
for produto, info in carrinho_compra.items():
    print(f"{produto}: {info['quantidade']} unidades x R$ {info['preco_unitario']:.2f} cada")
print(f"\nTotal do Carrinho: R$ {total_carrinho:.2f}")
