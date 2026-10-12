def obter_palpite():
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
        
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
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