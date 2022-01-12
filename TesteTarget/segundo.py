"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: 
	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

print('Sequência de Fibonacci')
print('--'*30)
print('--'*30)
print('--'*30)

n1 = 0
n2 = 1
n3 = 3
i = int(input('Digite um número que você acha que pertence a Sequência de Fibonacci: '))
print('--'*30)
print('--'*30)


while i > n3:
    n3 = n1 + n2
    n1 = n2
    n2 = n3

if i == 0:
    print('O número 0 está na Sequência de Fibonacci.')

elif i == n3:
    print('O número está na Sequência de Fibonacci.')

else:
    print('Esse número não faz parte da Sequência de Fibonacci.')

print('--'*30)
