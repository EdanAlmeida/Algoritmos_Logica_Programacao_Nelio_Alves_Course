"""
PROCESSAMENTO DE DADOS E CASTING EM PYTHON

EX:
    x = 5
    y = 3 * x

    print(y)
    print(x)

EX:
    b1 = 6.0
    b2 = 8.0
    h = 5.0
    area = ((b1 + b2) / 2.0) * h

    print(area)


EX:
    a: int
    b: int
    resultado: int

    a = 5
    b = 2
    resultado = a / b
    resultado2 = a // b

    print(resultado)
    # O python ignora a declaração e infere que deve exibir um 'float'
    print(resultado2)

"""

a: float
b: int

a = 5.2
b = a

print(b)
# Ele ignora a declaração e faz o que bem entende.

#Solução  -  CASTING
c = int(a)

print(c)
