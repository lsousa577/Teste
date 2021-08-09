import Funcoes as f
M = []

tam = int(input("digite o tamanho da matriz: "))
f.inicializa_matriz(tam, M)
f.adiciona_arestas(M)
f.mostra_graus(tam, M)
f.max_grau(tam, M)
f.min_grau(tam, M)
f.mostra_matriz(tam, M)

