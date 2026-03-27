# Questão 2 - Faça um programa que leia os dados de uma pessoa (Nome, RG, CPF, ano de nascimento e armazene em um arquivo txt, calculando a idade da pessoa.
import os
from datetime import datetime

print(os.getcwd())

nome = input("Digite o nome: ")
rg = input("Digite o RG: ")
cpf = input("Digite o CPF: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

with open('C:/Users/Aluno/Desktop/AtividadePython/ManipulacaoArquivos/info.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('---------------\n')
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"RG: {rg}\n")
    arquivo.write(f"CPF: {cpf}\n")
    arquivo.write(f"Ano de Nascimento: {ano_nascimento}\n")
    arquivo.write(f"Idade: {idade}\n")
    arquivo.write('---------------\n')

print("Dados salvos com sucesso.")