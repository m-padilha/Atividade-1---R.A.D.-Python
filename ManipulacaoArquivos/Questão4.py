# Questão 4 - Elabore um programa em Python que leia o nome e duas notas de um aluno do teclado, calcule a média e armazene em um arquivo text o nome, a média final e se o mesmo foi Aprovado(média >=6) ou Reprovado (média < 6).
import os
print(os.getcwd())

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

situacao = "Aprovado" if media >= 6 else "Reprovado"

with open('alunos.txt', 'a', encoding='utf-8') as arquivo: 
    arquivo.write('-------------------------------------------------------------\n')
    arquivo.write(f"Nome: {nome} | Média: {media:.2f} | Situação: {situacao}\n")
    arquivo.write('-------------------------------------------------------------\n')

print("Dados salvos com sucesso!")