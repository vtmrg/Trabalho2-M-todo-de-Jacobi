import numpy as np

from funcoes import iteracao, preencher_matriz_incognitas, jacobi2 #, matrizB, dividir_matriz
from mymat_until import ler_matriz, ler_dimensao


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
            dim_B = (dim_A[1], 1)
            matriz_B = ler_matriz("B", *dim_B)
            p = int(input("Digite o número de casas decimais (p): "))

            matriz_x = preencher_matriz_incognitas(dim_B[0])
            resultado = iteracao(matriz_A, matriz_B, p)

            print("Resultado da equação linear:")
            for i, valor in enumerate(resultado):
                print(f"x{i + 1} = {valor}")
        elif usuario == 2:

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
            dim_B = (dim_A[1], 1)
            matriz_B = ler_matriz("B", *dim_B)
            p = int(input("Digite o número de casas decimais (p): "))

            matriz_x = preencher_matriz_incognitas(dim_B[0])
            resultado = iteracao(matriz_A, matriz_B, p)
        
            sol= np.linalg.solve(matriz_A,matriz_B)
            print(sol)

            print("Resultado da equação linear:")
            for i, valor in enumerate(resultado):
                print(f"x{i + 1} = {valor}")
                
            diferenca = np.subtract(np.transpose(sol),np.transpose(resultado) )
    
            diferenca_quadrada = np.square(diferenca)
    
    
            erro_quadratico_medio = np.mean(diferenca_quadrada)
    
            print("Erro Quadrático Médio:", erro_quadratico_medio)

    else:
        print('\nEntrada inválida')
        resposta = input('\nEscolha: 1 - Voltar para o menu principal | Qualquer outra tecla - Sair do Programa')
        if int(resposta) == 1:
            func(log())
        else:
            print('\nO programa foi encerrado :)')
            return
