
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

        # if calcular_erro(x_ant, x, p):
        # return x

        x_ant = np.copy(x)  # Atualiza a matriz anterior com os valores atuais de x

    # Se o critério de convergência não for atendido após o número máximo de iterações
    print("O método de Jacobi não convergiu após o número máximo de iterações.")
    return None