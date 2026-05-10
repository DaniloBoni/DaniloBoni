import funcao

login = 'login'
cadastro = 'cadastro'

while True:
    print('\nJá possui Cadastro? ')
    print('Digite o Número')
    infoCadastro =int(input('1--Não ou 2--Sim: '))

    #CADASTRO
    if infoCadastro == 1:
        funcao.vericação_credenciais(cadastro)
    
    #LOGIN
    elif infoCadastro == 2:
        funcao.vericação_credenciais(login)
        funcao.buscar_videos()
        break
    
