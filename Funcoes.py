import numpy as np

'''Função para encontar matriz B'''

def matrizB(matriz):
    n = len(matriz)
    for i in range(n):
        diagonal_principal = matriz[i][i]
        for j in range(n):
            if i != j:
                matriz[i][j] /= diagonal_principal
            else:
                matriz[i][j] = 0
                matriz[i][j] *= -1
    return matriz

def dividir_matriz(matriz_coluna,matriz_quadrada):

    matriz_resultado = []
    for i in range(len(matriz_coluna)):
        elemento_diagonal = matriz_quadrada[i][i]
        elemento_coluna = matriz_coluna[i][0]
        resultado = elemento_coluna / elemento_diagonal
        matriz_resultado.append([resultado])

    return matriz_resultado



'''Função processo de iteração'''


def iteracao(A, x, g, p, max_iter=1000):
    n = len(A)
    x_ant = np.zeros_like(x)  # Cria uma matriz de zeros com as mesmas dimensões de x

    for k in range(max_iter):
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x_ant[j]
            x[i] = (g[i] - soma) / A[i][i]

        if erro_relativo(x_ant, x)> pow(10,-p):
          return x_ant

        else:
          x_ant = np.copy(x)  # Atualiza a matriz anterior com os valores atuais de x

    # Se o critério de convergência não for atendido após o número máximo de iterações
    print("O método de Jacobi não convergiu após o número máximo de iterações.")
    return None

def MSE(lista1,lista2):
    diferenca = numpy.subtract(lista1,  lista2)

    diferenca_quadrada = numpy.square(diferenca)

    erro_quadratico_medio = mean(diferenca_quadrada)

    return erro_quadratico_medio

def erro_relativo(xAnterior, xAtual):

    max01 = np.max(xAnterior)
    max02 = np.max(xAtual)
    erro = abs(max02 - max01) / max02

    return erro


def preencher_matriz_incognitas(num_colunas):
    matriz = []
    for i in range(num_colunas):
        incognita = 'x' + str(i + 1)
        matriz.append([incognita])
    return matriz
