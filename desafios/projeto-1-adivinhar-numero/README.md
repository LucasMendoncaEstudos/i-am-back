# 🎲 Projeto 1: Jogo de Adivinhar o Número

Jogo no terminal em que o computador sorteia um número e o jogador tenta descobrir qual é.

O projeto foi feito em **3 versões**, cada uma em um arquivo, cada uma mais completa que a anterior.

## 📁 Estrutura

```
projeto-1-adivinhar-numero/
├── README.md
├── v1_basico.py
├── v2_robusto.py
├── v3_avancado.py
└── recordes.json      # gerado automaticamente pela v3
```

## ▶️ Como rodar

```bash
python v1_basico.py
python v2_robusto.py
python v3_avancado.py
```

---

## Versão 1: Básico (`v1_basico.py`)

- [ ] O programa sorteia um número inteiro entre 1 e 100
- [ ] O jogador digita um palpite
- [ ] O programa informa se o número secreto é **maior** ou **menor**
- [ ] O jogo se repete até o jogador acertar
- [ ] Ao acertar, mostra em quantas tentativas o jogador conseguiu

## Versão 2: Robusto (`v2_robusto.py`)

- [ ] Limite de 7 tentativas
- [ ] Se as tentativas acabarem, o jogador perde e o programa revela o número secreto
- [ ] Tratar entradas inválidas (texto, vazio, número fora de 1-100) sem quebrar o programa
- [ ] Entrada inválida **não** gasta tentativa
- [ ] Ao final, perguntar "Quer jogar de novo? (s/n)"
- [ ] Código organizado em funções

## Versão 3: Avançado (`v3_avancado.py`)

- [ ] Escolha de dificuldade no início:

  | Nível   | Intervalo | Tentativas |
  |---------|-----------|------------|
  | Fácil   | 1 a 50    | 10         |
  | Médio   | 1 a 100   | 7          |
  | Difícil | 1 a 1000  | 10         |

- [ ] Salvar o recorde (menor nº de tentativas) em arquivo `.json`, um para cada dificuldade
- [ ] Ler o recorde ao iniciar e mostrá-lo ao jogador
- [ ] Avisar quando o jogador bater o recorde

---

## 🧠 Conceitos praticados

`input` / `print`, `int()`, `if/elif/else`, `while`, módulo `random`, `try/except`, funções, leitura e escrita de arquivos (`json`)

## 📏 Regras do desafio

- Escrever sem copiar código pronto
- Nomes de variáveis claros
- Testar os casos estranhos: `"abc"`, vazio, `0`, `101`, número negativo

## 📝 O que aprendi

> Preencher ao final: dificuldades, erros que travaram, o que faria diferente.
