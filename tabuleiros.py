def imprimir(tabuleiro):
    for l in range(0,11):
        for c in range(0,11):
            print(f' {tabuleiro[l][c]} ', end='')
        print()