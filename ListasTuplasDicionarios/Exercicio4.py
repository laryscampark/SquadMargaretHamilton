contatos = {
    'Laryssa': '21212121',
    'Pedro': '22222222',
    'Benjamin': '23232323',
    'Marley': '24242424'
}

def buscar(dicionario, nome):
    return dicionario.get(nome, 'Contato não encontrado.')

buscar_contato = input("Digite o nome do contato que deseja procurar: ")

resultado = buscar(contatos, buscar_contato)
print(f"Telefone de {buscar_contato}: {resultado}")
