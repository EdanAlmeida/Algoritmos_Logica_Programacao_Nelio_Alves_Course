"""
SAÍDA DE DADOS

- print;

versões antigas:
 - int = %d
 - float = %f
 - str = %s
 EX:
    x = 'Edan'
    y = 31

    print("%s tem %d anos" % (x, y))

print('Hello world! ', end='') #Evita a quebra de linha;
print('Boa noite!')


x = 10
y = 20
print(x)
print(y)

x: float
x = 2.3456
print("{:f}".format(x)) #Por padrão são 6 casas após a vírgula
print("{:.2f}".format(x)) #define o número de casas após a vírgula
"""

idade = 32
salario = 3100.00
nome = 'Maiara Iara Lara'

print(f'A funcionária {nome} tem {idade} anos e ganha R$ {salario:.2f}.')
#interpolação + correto
