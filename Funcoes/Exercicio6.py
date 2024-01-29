import random

def escolher():
    return random.choice(["python", "programacao", "jogoforca", "computador", "desenvolvimento"])

def jogar():
    segredo = escolher()
    correto = set()
    tentativas_maximas, tentativas = 6, 0

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas < tentativas_maximas:
        print("\nPalavra secreta:", ' '.join(letra if letra in correto else '_' for letra in segredo))
        letra = input("Informe uma letra: ").lower()

        if letra in correto:
            print("Você já tentou essa letra. Tente novamente.")
        elif letra in segredo:
            print("Letra correta! Continue assim.")
            correto.add(letra)
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas += 1

        if set(segredo) <= correto:
            print(f"Parabéns! Você adivinhou a palavra:{segredo}" )
            break

    else:
        print(f"Fim do jogo! Você excedeu o número máximo de tentativas. A palavra era: {segredo}")

if __name__ == "__main__":
    jogar()
