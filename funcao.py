import json
login = 'login'
cadastro = 'cadastro'
#                   cadastro/login 
def obter_credenciais(tipo_acao):

    print(f"\n----- {tipo_acao} -----")
    email = input('Digite seu email: ').strip()
    senha = input('Digite sua senha: ').strip()
    

    return email, senha

   #TESTES


# obter_credenciais(cadastro)

#                       cadastro/login    
def vericação_credenciais(tipo_acao): 

    usuarios = []
    while True:
        email, senha = obter_credenciais(tipo_acao)
        emailSenha_usuario = (f'{email}:{senha}') #usar no login

        with open('dados_Cadastros.txt', 'r') as dadosCadastro:

            for linha in dadosCadastro:
                
                formatdadosCadastro = linha.strip().split(':')
                usuarios.append(formatdadosCadastro)

            lista_email = []
            
            # CADASTRO
            if tipo_acao == 'cadastro':

                for credenciais in usuarios:
                    lista_email.append(credenciais[0])
                    
                if email in lista_email:#email
                    print('\n!!!Email já cadastrado!!!')
                    
                else:
                    with open('dados_Cadastros.txt', 'a') as dadosCadastro:
                        dadosCadastro.write(f'{email}:{senha}\n')
                        print(f"\n--- {tipo_acao} realizado! ---")
                        break

            lista_emailsenha = []
            #LOGIN
            if tipo_acao == 'login':
                
                with open('dados_Cadastros.txt', 'r') as dadosCadastro:
                    for linha in dadosCadastro:
                
                        email_senha_formatados = linha.strip()
                        lista_emailsenha.append(email_senha_formatados)

                    if emailSenha_usuario not in lista_emailsenha:
                        print('\n!!!Login/Senha incorretos!!!')
                    else:
                        print(f"\n--- {tipo_acao} realizado! ---")
                        print(f"\n--- Bem-vindo à plataforma! ---")
                        break
                

def buscar_videos():
    lista_nome_videos = []
    
    with open('dados_Nome_Videos.txt', 'r', encoding='utf-8') as dados_Nome_Videos:
        for linha in dados_Nome_Videos:
            lista_nome_videos.append(linha.strip())

    while True:
        print('\n')
        nomeVideo = input('Digite o nome do filme que deseja buscar: ').strip().lower()

        if nomeVideo not in lista_nome_videos:
            print('\n!!!filme não encontrado!!!')
        else: #achou o video
            with open('dados_Videos.json', 'r', encoding='utf-8') as dados_Videos:
                dadosVideosLidos = json.load(dados_Videos)
            
            info_videos(nomeVideo, lista_nome_videos, dadosVideosLidos)
            break
                # # Pegando o índice diretamente da lista
                # indice = lista_nome_videos.index(nomeVideo)
                # print(f'\n\n{dadosVideosLidos[indice]}')
                # break
           


def info_videos(nomeVideo, lista_nome_videos, dadosVideosLidos):
    while True:
        acoes = input('''
    Informações sobre o filme -- 1
    curtir --------------------- 2
    descurtir ------------------ 3
    buscar outro filme --------- 4
    sair ----------------------- 5
    ---> ''')

        if acoes == '1':
            print('\nInformações sobre o filme:\n')
            # Pega o índice diretamente da lista
            indice = lista_nome_videos.index(nomeVideo)
            informacao = dadosVideosLidos[indice]
            for chave, valor in informacao.items():
                print(f'{chave}: {valor}')
            acao = voltar_Acoes()
            if acao == 'voltar':
                continue
            elif acao == 'sair':
                break

        elif acoes == '2':
            with open('dados_Curtidas.json', 'r', encoding='utf-8') as dadosCurtidas:
                dadosCurtidasLidos = json.load(dadosCurtidas)

            indice = lista_nome_videos.index(nomeVideo)
            
            # O erro estava aqui: você precisa alterar o valor DENTRO da lista principal
            dadosCurtidasLidos[indice]['curtidas'] += 1
            
            print(f"\nVocê curtiu o filme! Total de curtidas: {dadosCurtidasLidos[indice]['curtidas']}")

            # E aqui você precisa salvar a LISTA INTEIRA (dadosCurtidasLidos) de volta no arquivo, e não apenas o número!
            with open('dados_Curtidas.json', 'w', encoding='utf-8') as dadosCurtidas:
                json.dump(dadosCurtidasLidos, dadosCurtidas, indent=4, ensure_ascii=False)
            acao = voltar_Acoes()
            if acao == 'voltar':
                continue
            elif acao == 'sair':
                break
            


        elif acoes == '3':
            with open('dados_Curtidas.json', 'r', encoding='utf-8') as dadosCurtidas:
                dadosCurtidasLidos = json.load(dadosCurtidas)

            indice = lista_nome_videos.index(nomeVideo)
            
            # Mesma lógica para descurtir
            dadosCurtidasLidos[indice]['descurtidas'] += 1
            
            print(f"\nVocê descurtiu o vídeo. Total de descurtidas: {dadosCurtidasLidos[indice]['descurtidas']}")

            with open('dados_Curtidas.json', 'w', encoding='utf-8') as dadosCurtidas:
                json.dump(dadosCurtidasLidos, dadosCurtidas, indent=4, ensure_ascii=False)
            acao = voltar_Acoes()
            if acao == 'voltar':
                continue
            elif acao == 'sair':
                break
        

        elif acoes == '4':
            buscar_videos()
            break


        elif acoes == '5':
            print('\n----Obrigado por usar a plataforma!----')
            break 
        
        elif acoes == '4':
            continue



def voltar_Acoes():
    acoesInfo = input('''
    \n
    voltar -- 1
    sair -- 4
    ---> ''')
        
    if acoesInfo == '1':
        return 'voltar'
    elif acoesInfo == '4':
        print('\n----Obrigado por usar a plataforma!----')
        return 'sair'