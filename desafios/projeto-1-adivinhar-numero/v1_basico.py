import random
from validador import obter_palpite

numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

tentativas = 0
while True:
    palpite = obter_palpite()
    
    if palpite is None:
        print(f"O número secreto era: {numero_secreto} e você fez {tentativas} tentativas.")
        break
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        if tentativas == 1:
            print(f"Parabéns! Você acertou o número secreto é: {numero_secreto}, você acertou em {tentativas} tentativa.")
            break
        else:
            print(f"Parabéns! Você acertou o número secreto é: {numero_secreto}, você acertou em {tentativas} tentativas.")
            break
    
