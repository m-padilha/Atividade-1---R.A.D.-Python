# Questão 1 - Elabore um programa em Python que leia uma cadeia de DNA e gera a cadeia inversa. Faça a leitura da cadeia utilizando arquivo txt.
import os
print(os.getcwd())

with open('dna.txt', 'r') as arquivo:
    cadeia = arquivo.read().strip()

cadeia_inversa = cadeia[::-1]

print("Entrada:", cadeia)
print("Saída:", cadeia_inversa) 