"""
ESTRUTURA CONDICIONAL EM PYTHON

Simples:
    - if condição:
        comando1
        comando2

Composta:
    - if condição:
        comando1
        comando2
    - else:
        comando3
        comando4

Encadeamento:
    - if condição1:
        comando1
        comando2
    -elif condição2:
        comando3
        comando4
    -else:
        comando5
        comando6

"""

hora = int(input('Digite uma hora do dia: '))

if hora < 12:
    print('Bom dia!')
elif (hora > 12) and (hora < 18):
    print('Boa tarde!')
else:
    print('Boa noite!')
