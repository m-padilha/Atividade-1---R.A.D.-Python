# Questão 5 - Faça um algoritmo em Python que leia dois números inteiros do teclado, faça uma mini calculadora (soma, subtração, multiplicação e divisão) e armazene todos os resultados em um arquivo txt.
import os
print(os.getcwd())

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro: divisão por zero"

with open('resultados.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('----------------\n')
    arquivo.write(f"Números: {num1} e {num2}\n")
    arquivo.write(f"Soma: {soma}\n")
    arquivo.write(f"Subtração: {subtracao}\n")
    arquivo.write(f"Multiplicação: {multiplicacao}\n")
    arquivo.write(f"Divisão: {divisao}\n")
    arquivo.write('----------------\n')