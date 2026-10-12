# ==========================================================
# DIA 2 — Calculadora de IMC
# ENUNCIADO: programa que pergunta peso (kg) e altura (m),
# calcula o IMC e mostra o valor + classificação:
# <18.5 abaixo do peso | 18.5 a 24.9 normal |
# 25 a 29.9 sobrepeso | >= 30 obesidade
# CONCEITOS: if/elif/else, operadores relacionais,
# float, formatação com :.2f
# ==========================================================

while True:
    try:
        altura = float(input('Digite sua altura(m): ').replace(',', '.'))
        if altura <= 0:
            print("A altura deve ser maior que zero. Tente novamente.")
            continue
        elif altura < 0.62 or altura > 2.55:
            print("A altura parece inválida. Por favor, digite uma altura válida.")
            continue
        break
    except ValueError:
        print("Por favor, digite números válidos para a altura.")

while True:
    try:
        peso = float(input('Digite seu peso(kg): ').replace(',', '.'))
        if peso <= 0:
            print("O peso deve ser maior que zero. Tente novamente.")
            continue
        elif peso < 25.4 or peso > 635:
            print("O peso parece inválido. Por favor, digite um peso válido.")
            continue
        break
    except ValueError:
        print("Por favor, digite números válidos para o peso.")
    
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
classificacao = "Classificação: "
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Classificação:{classificacao}")