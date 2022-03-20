"""
ESTRUTURA REPETITIVA ENQUANTO NO PYTHON

Sintaxe:
    - while condição:
        comando1
        comando2
Regra:
    - V = executa e volta
    - F = cai fora

"""

soma = 0
x = int(input('Digite o primeiro numero: '))

while x != 0:
    soma = soma + x
    x = int(input('Digite outro numero: '))

print(f'SOMA : {soma}')
