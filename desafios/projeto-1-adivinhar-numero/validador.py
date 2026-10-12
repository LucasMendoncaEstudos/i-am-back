def obter_palpite(minimo=1, maximo=100):
    while True:
        palpite = input("Digite seu palpite (ou 'sair' para sair): ").strip().lower()
        if palpite == 'sair':
            print("Saindo do jogo...")
            return None
        try:
            palpite = int(palpite)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        if palpite < minimo or palpite > maximo:
            print(f"Por favor, digite um número entre {minimo} e {maximo}.")
            continue
        
        return palpite    

def jogar_novamente():
    while True:
        resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'não', 'nao']:
            return False
        else:
            print("Por favor, digite 's' para sim ou 'n' para não.")
            
            
def menu():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Escolha seu Nivel de Dificuldade:\n1 - Fácil (10 tentativas no intervalor de 1 a 50)\n2 - Médio (7 tentativas no intervalo de 1 a 100)\n3 - Difícil (10 tentativas no intervalo de 1 a 1000)")
    nivel = int(input("Digite o número correspondente ao nível desejado: "))
    if nivel == 1:
        print("Você escolheu o nível Fácil. Você terá 10 tentativas para adivinhar o número secreto entre 1 e 50.")
    elif nivel == 2:
        print("Você escolheu o nível Médio. Você terá 7 tentativas para adivinhar o número secreto entre 1 e 100.")
    elif nivel == 3:
        print("Você escolheu o nível Difícil. Você terá 10 tentativas para adivinhar o número secreto entre 1 e 1000.")
    return nivel

