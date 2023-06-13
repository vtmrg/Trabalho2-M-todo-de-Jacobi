from funcoes import iteracao, matrizB, dividir_matriz




def log():

    print('\nEscolha uma opção (0 a 2): \n0-sair \n1- Inserir as esuqcaoes da forma Ax=b e calcular x(matriz de incógnitas) a partir do método de Jacobi \n2- Inserir as esuqcaoes da forma Ax=b e calcular x(matriz de incógnitas) a partir do método de Jacobi e depois calcular o MSE do resultado obtido com o resultado do método implementado por QuantStar')
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
            resposta = input('\nEscolha: 1-Voltar para o menu principal Qualquer outra tecla-Sair do Programa')
            if resposta == '1':
                return log()
            else:
                return 0


def func(digito):
    usuario = int(digito)
    if usuario == 0:
        print('\nO programa foi encerrado :)')
        return

    elif int(usuario)==1 or int(usuario)==2:

        if int(usuario) == 1:
          print('Preencha os valores A*x=B')
          dim_A = ler_dimensao("matriz A")
          print(len(dim_A))
          print(dim_A[0])
          print(dim_A[1])
          if (dim_A[1]) !=(dim_A[0]):
            print("As matrizes devem ter o mesmo número de linhas")
            resposta = input('\nEscolha: 1-Voltar para o menu principal -Sair do programa(qualquer outra tecla)')
            if int(resposta) == 1:
              func(1)
            else:
              print('\nO programa foi encerrado :)')
              return

          matriz_A = ler_matriz("A", *dim_A)
          dim_x = (len(dim_A), 1)
          dim_B = (len(dim_A), 1)
          matriz_B = ler_matriz("B", *dim_B)
          matrix=preencher_matriz_incognitas(dim_A[0])
          matrizbb=matrizB(matriz_A)
          matrizgg=dividir_matriz(matriz_B,matriz_A)
          print(matrizbb)
          print(matrizgg)

          p = int(input("Digite o número de casas decimais (p): "))

    # Resolução da equação linear utilizando o método de Jacobi
          resultado = iteracao(matrizbb, matriz_x, matriz_gg, p)

# Exibição dos resultados
          print("Resultado da equação linear:")
          for i in range(len(resultado)):
              print(f"x{i+1} = {resultado[i]}")





    else:
      print('\nEntrada inválida')
      resposta = input('\nEscolha: 1-Voltar para o menu principal Qualquer outra tecla-Sair do Programa')
      if int(resposta) == 1:
        func(log())
      else:
        print('\nO programa foi encerrado :)')
        return
