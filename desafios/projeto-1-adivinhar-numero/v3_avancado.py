import random
from validador import obter_palpite, jogar_novamente, menu


def jogar():
    nivel = menu()
    palpite = obter_palpite()
    if nivel == 1:
        numero_secreto = obter_palpite(1, 50)
        tentativas = 10
    elif nivel == 2:
        numero_secreto = obter_palpite(1, 100)
        tentativas = 7
    elif nivel == 3:
        numero_secreto = obter_palpite(1, 1000)
        tentativas = 10

    restantes = tentativas

    while tentativas > 0:

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
    jogar()
    if jogar_novamente():
        jogar()
    else:
        print("Obrigado por jogar! Até a próxima.")