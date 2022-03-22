"""
Leia 2 valores inteiros X e Y em qualquer ordem. A seguir, calcule e mostre a soma dos números ímpares entre eles.
--

"""

print('DIGITE DOIS NUMEROS INTEIROS: ')
x = int(input(' '))
y = int(input(' '))

if x > y:
    troca = x
    x = y
    y = troca

sum = 0
for i in range(x+1, y):
    if i % 2 != 0:
        sum = sum + i

print(f'SOMA DOS IMPARES: {sum}')
