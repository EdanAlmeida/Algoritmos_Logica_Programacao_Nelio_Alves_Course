"""
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor da área,
perímetro e diagonal deste retângulo, com quatro casas decimais:

"""
import math
base = float(input('Base do retangulo: '))
altura = float(input('Altura retangulo: '))

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = math.sqrt((base ** 2) + (altura ** 2))

print(f'AREA: {area:.4f}')
print(f'PERIMETRO: {perimetro:.4f}')
print(f'DIAGONAL: {diagonal:.4f}')
