import Banco as db
import time
while True: 
    print('_______Cadastro de Usuário:__________')
    print('''
        (1) Inserir da Dados
        (2) Atualizar Dados
        (3) Deletar Dados 
        (4) Consultar Dados
        (5) Consulta Dados Específico 
        (6) Sair do Progama
    ''')
    op =  int(input('Digite a Opção: '))
    if op == 1: 
        db.Banco_dados('Dados.db').Inserir_Dados(input('Usuario: '),input('Senha: '))
        print('Processando...')
        time.sleep(2)
    elif op == 2: 
        db.Banco_dados('Dados.db').Atualizar_Dados(input('Qual Usuario que atualizar: '),input('Novo Usuario: '),input('Nova Senha: '))
        print('Processando...')
        time.sleep(2)
    elif op == 3: 
        db.Banco_dados('Dados.db').Deletar_Dados(input('Nome do usuario: '))
        print('Processando...')
        time.sleep(2)
    elif op == 4: 
        lista = db.Banco_dados('Dados.db').Consulta_Dados()
        for item in lista:
            print(item)
            print()
            time.sleep(1)  
        time.sleep(2)
    elif op == 5: 
       print(db.Banco_dados('Dados.db').Consulta_Nome(input('Qual usuário deseja consultar: ')))
       print('Processando...')
       time.sleep(2)
    elif op == 6:
        break
    else: 
        print('Opção Invalida tente novamente...')

