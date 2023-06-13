

'''main ???'''

'''Leitura de três matrizes A, x e B, colocar saídas de texto'''
while resposta!=:
    print('Preencha os valores A*x=B')

    dim_A = ler_dimensao("matriz A")
    dim_x = (dim_A[0], 1)
    dim_B = dim_A

    if len(dim_A[0]) != len(dim_A[1]):
        print("As matrizes devem ter o mesmo número de linhas")
        resposta = input('\nEscolha: 1-Voltar para o menu principal -Sair do programa(qualquer outra tecla)')
        
        if int(resposta) == 1:
            func(3)

    else:
        print('\nO programa foi encerrado :)')
        return
    
    matriz_A = ler_matriz("A", *dim_A)
    matriz_x = criar_matriz(*dim_x)

    for i in range(dim_x[0]):
        matriz_x[i][0] = f'x{i+1}'

    print(matriz_x)
    matriz_B = ler_matriz("B", *dim_B)

    matrizbb=matrizB(matriz_A)
    print(matrizbb)

    p = int(input("Digite o número de casas decimais (p): "))

    # Resolução da equação linear utilizando o método de Jacobi
    resultado = iteracao(matrizbb, matriz_x, matriz_gg, p)

# Exibição dos resultados
print("Resultado da equação linear:")
for i in range(len(resultado)):
    print(f"x{i+1} = {resultado[i]}")
