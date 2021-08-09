
def inicializa_matriz(tam, M):

    for i in range(tam):
        linha = []
        for j in range(tam):
            linha.append(0)
        M.append(linha)

def mostra_matriz(tam, M):
    for i in range(tam):
        for j in range(tam):
            print(M[i][j], end = "|")
        print("")

def adiciona_arestas(M):
    resp = 's'
    while resp != 'n':
        l = int(input('Digite a linha: '))
        c = int(input('Digite a coluna: '))

        if l == c:
            M[l - 1][c - 1] += 1
        else:
            M[l - 1][c - 1] += 1
            M[c - 1][l - 1] += 1

        resp = input("Deseja adicionar mais uma aresta? [s/n] ")

def mostra_graus(tam, M):
    c = 1
    soma = 0
    for i in range(tam):
        for j in range(tam):
            soma += M[i][j]
        print(f'Quantidade de graus do V{c} é {soma}')
        c+=1
        soma = 0

def max_grau(tam, M):
    maxGrau = 0
    soma = 0
    for i in range(tam):

        for j in range(tam):
            soma += M[i][j]
        if maxGrau < soma:
            maxGrau = soma
        soma = 0
    print(f'o maior grau é {maxGrau}')

def min_grau(tam, M):

    soma = 0
    minGrau = 1000
    for i in range(tam):
        for j in range(tam):
            soma += M[i][j]

        if minGrau > soma:
            minGrau = soma
        soma = 0
    print(f'o menor grau é {minGrau}')