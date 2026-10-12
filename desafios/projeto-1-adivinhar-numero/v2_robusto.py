import random
from validador import obter_palpite, jogar_novamente


def jogar():
    numero_secreto = random.randint(1, 100)

    tentativas = 7
    restantes = tentativas

    while tentativas > 0:
        palpite = obter_palpite()

        if palpite is None:
            print(f"O número secreto era: {numero_secreto} e você fez {restantes - tentativas} tentativas.")
            break

        tentativas -= 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
            print(f"Você tem {tentativas} tentativas restantes.")

        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
            print(f"Você tem {tentativas} tentativas restantes.")

        elif palpite == numero_secreto:
            if tentativas == 6:
                print(f"Parabéns! Você acertou o número secreto é: {numero_secreto}, você acertou de primeira sobrando {tentativas} tentativas.")
            else:
                print(f"Parabéns! Você acertou o número secreto é: {numero_secreto}, você acertou em {restantes - tentativas} tentativas.")
            break

        if tentativas == 0:
            print(f"Suas tentativas acabaram! O número secreto era: {numero_secreto}.")


if __name__ == "__main__":
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print("Você tem 7 tentativas para acertar o número secreto.")
    
    jogar()
    if jogar_novamente():
        jogar()
    else:
        print("Obrigado por jogar! Até a próxima.")