"""
Fazer um programa para ler o nome e a idade de duas pessoas. Ao final, mostrar uma mensagem com os nomes e a idade
média entre essas pessoas, com uma casa decimal:

"""

print("DADOS DA PRIMEIRA PESSOA: ")
nome1 = input('Nome: ')
idade1 = float(input('Idade: '))

print("DADOS DA SEGUNDA PESSOA: ")
nome2 = input('Nome: ')
idade2 = float(input('Idade: '))

media = (idade1 + idade2) / 2

print(f'A idade media entre {nome1} e {nome2} eh de {media:.1f} anos.')
