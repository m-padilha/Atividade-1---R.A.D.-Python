# Questão 2 - Faça um programa que leia um texto de um arquivo txt e conte quantas palavras tem nesse arquivo, sem considerar os espaços.
import os
print(os.getcwd())

with open('texto.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.split()
quantidade = len(palavras)
print("Número de palavras:", quantidade)