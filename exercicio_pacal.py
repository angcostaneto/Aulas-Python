def imprimeColuna(n):
    for numero in range(1, n+1):
        for linha in range(1, numero+1):
            print(linha, end=' ')
        print('')

imprimeColuna(10)

