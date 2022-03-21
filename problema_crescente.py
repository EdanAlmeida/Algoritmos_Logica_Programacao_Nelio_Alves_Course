"""
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que
indique se estes valores foram digitados em ordem crescente ou decrescente. O programa deve finalizar quando forem
digitados dois valores iguais.

"""

print('DIGITE DOIS VALORES INTEIROS: ')
x = float(input(' '))
y = float(input(' '))

while x != y:
    if x < y:
        print('CRESCENTE!')
        print('DIGITE OUTROS DOIS NUMEROS INTEIROS: ')
        x = float(input(' '))
        y = float(input(' '))
    else:
        print('DECRESCENTE!')
        print('DIGITE OUTROS DOIS NUMEROS INTEIROS: ')
        x = float(input(' '))
        y = float(input(' '))
