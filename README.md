# Trabalho 2 - Método Numéricos 2023/1
## Método de Jacobi para Resolução de Equações Lineares

Este é um código simples que implementa o método de Jacobi para resolver sistemas de equações lineares. O método de Jacobi é um método iterativo para encontrar soluções aproximadas de sistemas lineares.

### Descrição

O método de Jacobi é baseado na decomposição de uma matriz A em uma matriz diagonal D, uma matriz triangular inferior L e uma matriz triangular superior U. O sistema de equações lineares Ax = b é reescrito como (D + L + U)x = b. Em cada iteração, o método de Jacobi atualiza os valores de x usando a fórmula:

<p align="center"> <img width="708" alt="Captura de Tela 2023-06-10 às 17 59 11" src="https://github.com/vtmrg/Trabalho2-M-todo-de-Jacobi/assets/127882225/a9e4de56-409a-4ffa-92e8-312d099fe5d4">
  </p>

O processo é repetido até que um critério de convergência seja atingido, como um número máximo de iterações ou um erro relativo abaixo de um determinado limite.


<p align="center"> <img width="353" alt="Captura de Tela 2023-06-10 às 18 09 57" src="https://github.com/vtmrg/Trabalho2-M-todo-de-Jacobi/assets/127882225/d9a914d3-2134-4a7d-bca6-1757fab0e349">
</p>
