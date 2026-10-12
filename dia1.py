# ==========================================================
# DIA 1 — Dados pessoais e idade futura
# ENUNCIADO: programa que pergunta nome, idade e cidade
# e imprime uma frase com os dados e a idade da pessoa
# daqui a 10 anos.
# CONCEITOS: input, conversão de tipos (int), f-strings,
# validação de entrada com while + isdigit()
# ==========================================================

nome = input("Qual o seu Nome ? ")
while True:
    idade = input("Qual a sua idade?: ")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("Por favor, digite um número válido para a idade.")
cidade = input("Qual a sua cidade: ")

print(f"{nome},{idade} anos, mora em {cidade}. Daqui a 10 anos terá {idade + 10}")
