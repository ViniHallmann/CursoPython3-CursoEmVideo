#Crie um módulo chamado moeda.py que tenha as funções incorporadas 
#aumentar(), diminuir(), dobro() e metade(). 
#Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
valor = float(input("Digite o preco: R$"))
print(f'A metade de R${valor} e R${moeda.metade(valor)}')
print(f'O dobro de R${valor} e R${moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor)+valor}')
