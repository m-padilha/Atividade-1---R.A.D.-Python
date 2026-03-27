# Questão 1 - Elabore um programa em Python que insere a tabuada de multiplicação de 9 em um arquivo txt.
import os
print(os.getcwd())

with open('tabuada_9.txt', 'a') as arquivo:
    arquivo.write('------------\n')
    for i in range(1, 11):
        tabuada = f"9 x {i} = {9 * i}\n"
        arquivo.write(tabuada)
    arquivo.write('------------\n')
