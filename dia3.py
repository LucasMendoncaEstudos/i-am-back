# ==================================================================
# DIA 3 — Estatísticas de 5 números
# ENUNCIADO: ler 5 números e mostrar o maior, o menor e a média.
# CONCEITOS: for, range, acumuladores (maior/menor manual),
# validação com while + isdigit (só inteiros positivos, por decisão)
# ===================================================================

numeros = []
for c in range(1,6):
    while True:
        entrada = input(f"Digite o {c}° número: ")
        
        if entrada.isdigit():
            entrada = int(entrada)
            numeros.append(entrada)
            if c ==1:
                maior = menor = entrada
            else:
                if entrada > maior:
                    maior = entrada
                if entrada < menor:
                    menor = entrada
            break
        else:
            print("Digite um número inteiro válido!")

"""
versão atualizada
maior = max(numeros)
menor = min(numeros)"""

media = sum(numeros)/len(numeros)

print(f"Na lista de numeros :{numeros}\nO maior numero é o {maior}\nO menor numero é o {menor}\nE a média deles seria {media:.2f}")