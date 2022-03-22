"""
Faça um programa que leia 'N' números reais e armazene-os em um vetor. Em seguida:
    - imprimir todos os elementos do vetor;
    - mostrar na tela a soma e a média dos elementos do vetor./
--
"""

n = int(input('Quantos numeros voce vai digitar? '))
vet = [0 for x in range(n)]

sum = 0
for i in range(0, n):
    vet[i] = float(input('Digite um numero: '))
    sum = sum + vet[i]

media = sum / n

print()
print('VALORES = ', end='')
for i in range(0, n):
    print(f'{vet[i]:.2f} ', end='')

print()
print(f'SOMA = {sum}')
print(f'MEDIA = {media}')
