login = input('Informe seu login: ')
senha = input('Informe sua senha: ')

if login == 'admin' and senha == 'admin123':
    print(f'O login foi {login} e a senha foi {senha} o acesso foi liberado')
else:
    print(f'O login foi {login} e a senha foi {senha} o acesso foi negado')