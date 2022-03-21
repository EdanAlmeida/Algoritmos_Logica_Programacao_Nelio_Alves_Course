"""
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três números lidos.
em caso de empate, mostrar apenas uma vez.

"""

print('DIGITE TRES NUMEROS INTEIROS: ')
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Terceiro numero: '))
menor = 0

if (num1 < num2) and (num1 < num3):
    menor = num1
elif (num2 < num3):
    menor = num2
else:
    menor = num3

print(f'MENOR: {menor}')
