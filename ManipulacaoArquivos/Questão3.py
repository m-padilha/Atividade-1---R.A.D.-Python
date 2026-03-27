# Questão 3 - Faça um programa que leia um arquivo txt e insere cada linha em uma lista.
import os
print(os.getcwd())

linhas = []

with open('lista.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    for linha in arquivo:
        linhas.append(linha.strip())

print(linhas)