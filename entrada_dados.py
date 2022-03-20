"""
ENTRADA DE DADOS EM PYTHON

INPUT
- pode colocar um texto junto ao input já;
- no entanto, o comando input é para ler dados do tipo 'str';
- precisa especificar (tipo um casting) para que ele leia outros tipos de dados

"""

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

print(f'Seu nome e {nome} e sua idade e {idade} anos')
