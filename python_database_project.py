import os
import sqlite3 as db
import pandas as pd

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nomeI = nome
        self.idadeI = idade
        self.profissaoI = profissao

    def obterNome(self):
        return self.nomeI
    
    def obterIdade(self):
        return self.idadeI

    def obterProfissao(self):
        return self.profissaoI

    def alterarNome(self, newNome):
        self.nomeI = newNome
        return self.nomeI
    
    def alterarIdade(self, newIdade):
        self.idadeI = newIdade
        return self.idadeI

    def alterarProfissao(self, newProfissao):
        self.profissaoI = newProfissao
        return self.profissaoI
objPessoas = []

connection = db.connect('dados.db')
cursor = connection.cursor()
try:
    cursor.execute('CREATE TABLE dados(nome TEXT, idade INTEGER, profissao TEXT)')
except:
    os.remove('dados.db')
finally:
    print('Base de dados criada.')

    read_db = cursor.execute('SELECT * FROM dados').fetchall()
    if len(read_db) == 0:
        print('Não existem dados na base de dados.')
    else:
        for i in read_db:
            objPessoas.append(Pessoa(i[0], i[1], i[2]))

def listaPessoas(objPessoas):
    for i in range(len(objPessoas)):
        print('************ Opção ' + str(i) + ' *************')
        print('Nome:' + str(objPessoas[i].obterNome()[0]) +
        '\n' + 'Idade:' + str(objPessoas[i].obterIdade()) + '\n' +
        'Profissão:' + str(objPessoas[i].obterProfissao()))
    opcaoNome = input('Introduza o número correspondente à pessoa que quer alterar: ')
    try:
        iOpcaoNome = int(opcaoNome)
        if iOpcaoNome >= len(objPessoas):
            print('Introduza um número dentro das opções disponíveis.')
            iOpcaoNome = -1
    except:
        iOpcaoNome = -1
        print('Introduza o número correto.')
    finally:
        return iOpcaoNome

while True:
    print('\n****************************************')
    print('************ Base de dados *************')
    print('****************************************\n')
    print('C - Consultar pessoas')
    print('A - Adicionar pessoas')
    print('N - Alterar nome')
    print('I - Alterar idade')
    print('P - Alterar profissão')
    print('E - Exportar ficheiro CSV')
    print('X - Sair\n')
    opcao = input('Escolha uma opção: ')

    if opcao == 'C' or opcao == 'c':
        if len(objPessoas) == 0:
            print('\nNão existem pessoas adicionadas.')
        else:
            print('\n**********************************************')
            print('************ Consulta de pessoas *************')
            print('**********************************************\n')
            for i in range(len(objPessoas)):
                print('Nome: ' +objPessoas[i].obterNome())
                print('Idade: ' + objPessoas[i].obterIdade())
                print('Profissão: ' + objPessoas[i].obterProfissao())
                print('\n-------------------------------------------')
        input('Pressione Enter para continuar.')
        clear = lambda: os.system('cls')
        clear()

    elif opcao == 'A' or opcao == 'a':
        print('\n*********************************************')
        print('************ Introduzir pessoas *************')
        print('*********************************************\n')
        nome = input('Introduza o nome: ')
        idade = input('Introduza a idade: ')
        profissao = input('Introduza a profissão: ')
        objPessoas.append(Pessoa(nome, idade, profissao))
        cursor.execute(f"INSERT INTO dados VALUES('{nome}', '{idade}', '{profissao}')")
        connection.commit()
        print('\nNova pessoa introduzida.')
        input('Pressione Enter para continuar.')
        clear = lambda: os.system('cls')
        clear()

    elif opcao == 'N' or opcao == 'n':
        if len(objPessoas) == 0:
            print('\nNão existem pessoas adicionadas.')
            input('Pressione Enter para continuar.')
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                nome = input('Introduza o novo nome: ')
                objPessoas[iOpcaoNome].alterarNome(nome)
                print('Nome da pessoa alterado.')
                input('Pressione Enter para continuar.')
                clear = lambda: os.system('cls')
                clear()
            input('Pressione Enter para continuar.')
            clear()

    elif opcao == 'I' or opcao == 'i':
        if len(objPessoas) == 0:
            print('\nNão existem pessoas adicionadas.')
            input('Pressione Enter para continuar.')
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                idade = input('Introduza a nova idade: ')
                objPessoas[iOpcaoNome].alterarIdade(idade)
                
                print('Idade da pessoa alterada.')
                input('Pressione Enter para continuar.')
                clear = lambda: os.system('cls')
                clear()

    elif opcao == 'P' or opcao == 'p':
        if len(objPessoas) == 0:
            print('\nNão existem pessoas adicionadas.')
            input('Pressione Enter para continuar.')
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                profissao = input('Introduza a nova profissão: ')
                objPessoas[iOpcaoNome].alterarProfissao(profissao)
                print('Profissão da pessoa alterada.')
                input('Pressione Enter para continuar.')
                clear = lambda: os.system('cls')
                clear()
    
    elif opcao == 'E' or opcao == 'e':
        if len(objPessoas) == 0:
            print('\nNão existem pessoas adicionadas.')
            input('Pressione Enter para continuar.')
            clear = lambda: os.system('cls')
            clear()
        else:
            connection = db.connect('dados.db')
            dbdf = pd.read_sql("SELECT * FROM dados",connection)
            connection.close()
            dbdf.to_csv('dados.csv',index=False)

    elif opcao == 'X' or opcao == 'x':
        break
