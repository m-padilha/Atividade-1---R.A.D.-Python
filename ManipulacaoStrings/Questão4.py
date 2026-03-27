# Questão 4 - Elabore um script em Python que leia um arquivo contendo frases e insira cada palavra da frase lida em uma lista, sem que haja palavras repetidas.
import os
print(os.getcwd())

with open('repeticao.txt', "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

palavras = conteudo.split()

lista_sem_repeticao = []
for palavra in palavras:
    if palavra not in lista_sem_repeticao:
        lista_sem_repeticao.append(palavra)

print(lista_sem_repeticao)
