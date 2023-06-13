import numpy as np

def criar_matriz(linhas, colunas, celula=0):
    m = [0] * linhas
    for i in range(len(m)):
        m[i] = [celula] * colunas
    return m

def ler_matriz(nome, linhas, colunas):
    print(f"Dados da matriz {nome}:")
    m = criar_matriz(linhas, colunas)
    for i in range(len(m)):
        for j in range(len(m[i])):
            while True:
                try:
                    m[i][j] = float(input(f"   - célula [{i}][{j}]: "))
                    break
                except ValueError:
                    print("Erro: o valor digitado não é um número válido. Tente novamente.")
    return m

def ler_dimensao(nome):
    print(f"Para a {nome}, qual a dimensão?")
    lin = int(input("   - quantidade de linhas: "))
    col = int(input("   - quantidade de colunas: "))
    return lin, col

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

def dividir_matriz(matriz_coluna, matriz_quadrada):
    matriz_resultado = []
    for i in range(len(matriz_coluna)):
        elemento_diagonal = matriz_quadrada[i][i]
        elemento_coluna = matriz_coluna[i][0]
        resultado = elemento_coluna / elemento_diagonal
        matriz_resultado.append([resultado])
    return matriz_resultado

def preencher_matriz_incognitas(num_colunas):
    matriz = []
    for i in range(num_colunas):
        incognita = 'x' + str(i + 1)
        matriz.append([incognita])
    return matriz

def iteracao(A, x, g, p, max_iter=1000):
    n = len(A)
    x_ant = np.zeros_like(x)

    for k in range(max_iter):
        for i in range(n):
            soma = 0.0
            for j in range(n):
                if i != j:
                    soma += A[i][j] * x_ant[j]
            x[i] = (g[i] - soma) / A[i][i]

        if erro_relativo(x_ant, x) > pow(10, -p):
            return x_ant
        else:
            x_ant = np.copy(x)

    print("O método de Jacobi não convergiu após o número máximo de iterações.")
    return None

def erro_relativo(xAnterior, xAtual):
    max01 = np.max(xAnterior)
    max02 = np.max(xAtual)
    erro = abs(max02 - max01) / max02
    return erro

def log():
    print('\nEscolha uma opção (0 a 2): \n0 - sair \n1 - Inserir as equações da forma Ax=b e calcular x (matriz de incógnitas) a partir do método de Jacobi \n2 - Inserir as equações da forma Ax=b e calcular x (matriz de incógnitas) a partir do método de Jacobi e depois calcular o MSE do resultado obtido com o resultado do método implementado por QuantStar')
    user = input()

    try:
        user = int(user)
        return user
    except ValueError:
        if user.strip() == '':
            print('\nNenhuma entrada fornecida. Saindo do programa.')
            return 0
        else:
            print('\nEntrada inválida')
            resposta = input('\nEscolha: 1 - Voltar para o menu principal | Qualquer outra tecla - Sair do Programa')
            if resposta == '1':
                return log()
            else:
                print('\nO programa foi encerrado :)')
                return 0

def func(digito):
    usuario = int(digito)
    if usuario == 0:
        print('\nO programa foi encerrado :)')
        return

    elif usuario == 1 or usuario == 2:
        if usuario == 1:
            print('Preencha os valores A*x=B')
            dim_A = ler_dimensao("matriz A")
            if dim_A[1] != dim_A[0]:
                print("As matrizes devem ter o mesmo número de linhas")
                resposta = input('\nEscolha: 1 - Voltar para o menu principal | Qualquer outra tecla - Sair do programa')
                if int(resposta) == 1:
                    func(1)
                else:
                    print('\nO programa foi encerrado :)')
                    return

            matriz_A = ler_matriz("A", *dim_A)
            dim_x = (dim_A[1], 1)
            dim_B = (dim_A[1], 1)
            matriz_B = ler_matriz("B", *dim_B)
            matriz_x = criar_matriz(*dim_x)
            matriz_gg = dividir_matriz(matriz_B, matriz_A)
            matriz_bb = matrizB(matriz_A)
            print(matriz_bb)
            print(matriz_gg)
            p = int(input("Digite o número de casas decimais (p): "))

            resultado = iteracao(matriz_bb, matriz_x, matriz_gg, p)

            print("Resultado da equação linear:")
            for i in range(len(resultado)):
                print(f"x{i + 1} = {resultado[i]}")

    else:
        print('\nEntrada inválida')
        resposta = input('\nEscolha: 1 - Voltar para o menu principal | Qualquer outra tecla - Sair do Programa')
        if int(resposta) == 1:
            func(log())
        else:
            print('\nO programa foi encerrado :)')
            return

opcao = 1
while opcao != 0:
    opcao = log()
    func(opcao)

