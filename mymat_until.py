'''Funções de ler/criar matriz'''

# cria e retorna uma matriz (linhas x colunas) com conteúdo celula (ou zero por default)
def criar_matriz(linhas, colunas, celula=0):
    m = [0] * linhas
    for i in range(len(m)):
        m[i] = [celula] * colunas
    return m

# criar e depois lê uma matriz (linhas x colunas)
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

# le as dimensões (linha e coluna) e retorna como tupla
def ler_dimensao(nome):
    print(f"Para a {nome}, qual a dimensão?")
    lin = int(input("   - quantidade de linhas: "))
    col = int(input("   - quantidade de colunas: "))
    return lin, col  # retorna uma tupla

# Função pronta Jacobi
def jacobi(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x
