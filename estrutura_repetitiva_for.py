"""
ESTRUTURA REPETITIVA PARA EM PYTHON

Sintaxe:
    - for variavel in range(valor_inicial, valor_final, [passo]):
        comando1
        comando2

Regra:
    - Primeira vez = variável assume o valor inicial
    - Repetição = se a variável for menor que o valor_final, executa e repete, senão pula fora
    - Na volta = incrementa a variável de '1' ou do valor de 'passo' se houver

EX:
    for i in range(0, 5): # O passo entraria no parenteses = (0, 5, 2) - pulando de dois em dois
        print(i)
"""

n = int(input('Quantos numeros serao digitados? '))

soma = 0

for i in range(0, n):
    x = int(input('Digite um numero: '))
    soma = soma + x

print(f'SOMA: {soma}')

# a variável i começa em 0.
