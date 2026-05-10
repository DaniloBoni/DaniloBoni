import funcao


#tipo de ações ----
login = 'login'
cadastro = 'cadastro'

#tipo de DADOS ----
email = 'email'
senha = 'senha'

#cadastro usuarios
print('Já possui Cadastro? ')
print('Digite o Número')
infoCadastro =int(input('1--Não ou 2--Sim: '))
 

#não possui cadastro (Cadastro)
if infoCadastro == 1:
    with open('dados_Login.txt', 'a') as dadosLogin:
            email, senha = funcao.obter_credenciais(cadastro)  #2 variaveis -> capturando os valores
            
    try: #------------------------------ verificação do email
            if email in dadosLogin:
                while email in dadosLogin:
                
                    print()
                    print('Já possui esse email cadastrado!!')
                    email = input('Digite o email: ')
                    senha = input('Digite a senha: ')
                
                else: 
                    print()
                    print('Email Cadastrado com SUCESSO !!')
                    discLogin.update({email: senha})
                    
                    # break
            else:
                print()
                ('Email Cadastrado com SUCESSO !!')
                discLogin.update({email: senha})#
    except:
         print('\n ERRO no cadastro!')
                
                

#possui o cadastro (login)
elif infoCadastro == 1:
    
    print()
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

#verificação da senha
    while True:
        if email in discLogin: #
            if discLogin[email] == senha:##
                print()
                print('Login efetuado com sucesso!!')#-------------------------
                break

            else:
                print()
                print('Senha incorreta!!')
                senha = input('Digite sua senha: ')
                
                

        #se errar o email
        else:
            print()
            print('Email INCORRETO !!')
            email = input('Digite um email válido : ')
            

            if email in discLogin:#
                senha = input('Digite sua senha: ')

                if discLogin[email] == senha:#
                    print()
                    print('Login encontrado!!')
                    break

            else:
                print()
                print('Email INCORRETO !!')
                email = input('Digite um email válido : ')




    
        
print(discLogin)#




