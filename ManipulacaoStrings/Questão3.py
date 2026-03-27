# Questão 3 - Faça um programa em Python que lê um texto de um arquivo txt e substitua todos os espaços por underline (_)
import os
print(os.getcwd())

with open('substituicao.txt', "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

conteudo_modificado = conteudo.replace(" ", "_")

with open('substituicao.txt', "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_modificado)

print("Arquivo modificado com sucesso!")
