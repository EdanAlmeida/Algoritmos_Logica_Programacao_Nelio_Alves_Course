"""
VETORES EM PYTHON

Declaração:
    - meu_vetor: [tipo] = [0 for x in range(nº elementos)]

- Na verdade, o Python trabalha com listas/tuplas/dicionários/conjuntos etc.
- O exemplo abaixo é uma lista.
- as listas em Python não são homogêneas

"""

n = int(input('Quantos numeros voce vai digitar? '))
vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input('Digite um numero: '))

print()
print('NUMEROS DIGITADOS: ')

for i in range(0, n):
    print(f'{vet[i]:.1f}')
