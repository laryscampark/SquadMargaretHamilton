resposta = 0
pergunta = input('Telefonou para a vítima? (sim ou não) ');
if pergunta == "sim":
    resposta += 1

pergunta = input('Esteve no local do crime? (sim ou não) ');
if pergunta == "sim":
    resposta += 1

pergunta = input('Mora perto da vítima? (sim ou não) ');
if pergunta == "sim":
    resposta += 1

pergunta = input('Devia para a vítima? (sim ou não) ');
if pergunta == "sim":
    resposta += 1

pergunta = input('Já trabalhou com a vítima? (sim ou não) ');
if pergunta == "sim":
    resposta += 1

        
    if resposta == 2:
        print('Pessoa considerada suspeita')
    elif 3 <= resposta <= 4:
        print('Pessoa considerada cúmplice')
    elif resposta == 5:
        print('Pessoa considerada assassino')
    else:
        print('Pessoa considerada inocente')    
    