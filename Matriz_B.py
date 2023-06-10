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
