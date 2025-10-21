from time import sleep

#SISTEMA DE USO DE CORES ANSI. EU USO A CHAVE PARA INFORMAR A COR (NO CASO DE CORES APLICADOS SOBRE O TEXTO) E AS CHAMO PELO SEU VALOR, DENTRO DO DICIONÁRIO.
# O CÓDIGO DA COR É APLICADO NA STRING QUE ESTOU FORMATANDO, SEJA PARA O TETXO OU PARA O FUNDO.

cor_texto = {'branco': '\033[30m', 'vermelho': '\033[31m',
              'verde': '\033[32m', 'amarelo': '\033[33m',
              'azul': '\033[34m', 'roxo': '\033[35m',
              'azulfraco': '\033[36m', 'cinza': '\033[37m'}

texto_formato = {'none': '\033[m', 'grifado': '\033[1m', 'sublinhado': '\033[4m', 'invertido': '\033[7m'}

cor_fundo = {'branco': '\033[40m', 'vermelho': '\033[41m',
              'verde': '\033[42m', 'amarelo': '\033[43m',
              'azul': '\033[44m', 'roxo': '\033[45m',
              'azulfraco': '\033[46m', 'cinza': '\033[47m'}


# FUNÇÃO PARA RETORNAR SEMPRE UM INTERIO, TRATANDO ESPAÇOS VAZIOS, PONTOS FLOAT E STRINGS.
def validar_codigo(msg: str, minimo: int = 6):
    while True:
        erros_codigo = []
        numero = input(msg).strip()
        try:
            if not numero or numero == '' or ' ' in numero:
                erros_codigo.append(f'{cor_texto['vermelho']}-Erro, caixa vazia ou com espaços!\033[m')
            if len(numero) < minimo:
                erros_codigo.append(f'{cor_texto['vermelho']}-Erro, o código deve ter ao menos\033[m \033[34m{minimo}\033[m \033[31mdígitos!\033[m')
            if not numero.isdigit():
                erros_codigo.append(f'{cor_texto['vermelho']}-Erro, digite apenas números!\033[m')
            if erros_codigo:
                print(f'{cor_texto['vermelho']}-Erro(s) encontrado(s) no código:\033[m\n')
                for e in erros_codigo:
                    sleep(0.3)
                    print(f'{e}\n')
                    continue
            else:
                return int(numero)
        except ValueError:
            continue

#SISTEMA DE VALIDAÇÃO DE SENHA SEGURA. A FUNÇÃO IRÁ TESTAR UMA SÉRIE DE CONDIÇÕES COMO: LETRA MAIÚSCULA, MINÚSCULA, DÍGITO, SÍMBOLO... E, APÓS ISSO, VALIDAR ELA.

def validar_senha(msg: str, tamanho_senha: int = 6):
    while True:                                                                                                         # Uso de while True para que o usuário sempre tenha a chance de acessar a conta.
        password = input(msg).strip()                                                                                   # Variavel que recebe o input da senha.
        erros_senha = []                                                                                                # Vetor que recebe os erros acumulados em cada if, alocados atraves do método 'append'
        simbolos = '\033[35m@#$%^&*()-_=+[]{};:,.?/\\|'                                                                 # Símbolos aceitos na validação de senha.
        contar_erros_senha = 0                                                                                          # Soma a quantidade de erros que o usuário cometeu, vindo após isso os erros em si (erros_senha).

        # SÉRIE DE CRITÉRIOS PARA UMA SENHA FORTE. USO DO ANY PARA VALIDAR PELO MENOS UM 1 CRITÉRIO DA CONDIÇÃO DENTRO DA SENHA
        if not any(c.isupper() for c in password):
            erros_senha.append(f'{cor_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mCARACTERE MAIÚSCULO!\033[m')
            contar_erros_senha += 1
        if not any(c.islower() for c in password):
            erros_senha.append(f'{cor_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mCARACTERE MINÚSCULO!\033[m')
            contar_erros_senha += 1
        if not any(c.isdigit() for c in password):
            erros_senha.append(f'{cor_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m1\033[m \033[31mDÍGITO!\033[m')
            contar_erros_senha += 1
        if len(password) < tamanho_senha:
            erros_senha.append(f'{cor_texto['vermelho']}A SENHA DEVE CONTER AO MENOS\033[m \033[34m{tamanho_senha}\033[m \033[31mCARACTERES!\033[m')
            contar_erros_senha += 1
        if not any(c in simbolos for c in password):
            erros_senha.append(f'{cor_texto['vermelho']}A SENHA DEVE CONTER ALGUM SÍMBOLO ESPECIAL! \033[m' + simbolos)
            contar_erros_senha += 1
        if erros_senha:                                                                                                 # Condição para ser possível exibir os erros e a sua soma. o else abaixo verifica a inexistência dos erros, retornando, assim, "password'.
            if contar_erros_senha == 1:
                sleep(0.5)
                print(f'{cor_texto['cinza']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(f'{cor_texto['vermelho']}{contar_erros_senha}\033[m \033[37mERRO ENCONTRADO NA SUA SENHA:\033[m\n')
                sleep(0.5)
                for erro in erros_senha:
                    sleep(0.5)
                    print(erro)
                print(f'{cor_texto['verde']}### TENTE NOVAMENTE! ###\033[m\n')
            else:
                sleep(0.5)
                print(f'{cor_texto['cinza']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(f'{cor_texto['vermelho']}{contar_erros_senha}\033[m \033[37mERROS ENCONTRADOS NA SUA SENHA:\033[m\n')
                for erroS in erros_senha:
                    sleep(0.5)
                    print(erroS)
                print(f'{cor_texto['verde']}### TENTE NOVAMENTE! ###\033[m\n')
                sleep(0.5)
        else:
            sleep(0.5)
            print(f'{cor_texto['verde']}{texto_formato['sublinhado']}SENHA CRIADA COM SUCESSO\033[m')
            return password

#SISTEMA DE VALIDAÇÃO DE FORMATO DE EMAIL. SÃO TESTADAS UMA SÉRIE DE CRITÉRIOS QUE OS ENDEREÇOS ELETRÓNICOS GERALMENTE DEVEM POSSUIR.
#OBS cada if é testado separadamente, sem uso de elif, pois os erros serão armazenados num vetor.

def validar_emaill(mg: str, tamanho_email: int = 10):
    while True:                                                                                                         #while True para o restante da função, pois os critérios devem ser atentidos, podendo ser possível refazer o processo caso o usuário erre em algum critério.
        contar_erros_email = 0                                                                                          # Variável para soma dos erros dos usuário na criação do email.
        erros_email = []                                                                                                # Vetor onde é armazenado os erros cometidos pelo usuário na criação do email.
        emai = input(mg).strip().lower()                                                                                # A funão lower é usada para ignorar maiusculas, de forma que se o usuário cria um email "XXX', ele pode acessar como 'XxX'.

        # SÉRIE DE CRITÉRIOS ('@', SEM DOIS PONTOS SEGUIDOS '..' ETC) QUE OS EMAILS NORMALMENTE POSSUEM.
        if not emai:
            erros_email.append(f'{cor_texto['vermelho']}ERRO, ESPAÇO VAZIO!\033[m')
            contar_erros_email += 1
        if ' '  in emai:
            erros_email.append(f'{cor_texto['vermelho']}NÃO PODE CONTER ESPAÇOS!\033[m')
            contar_erros_email += 1
        if len(emai) < tamanho_email:
            erros_email.append(f'{cor_texto['vermelho']}O EMAIL DEVE CONTER AO MENOS\033[m \033[34m{tamanho_email}\033[m \033[31mCARACTERES!\033[m')
            contar_erros_email += 1
        if not '@' in emai:
            erros_email.append(f'{cor_texto['vermelho']}O EMAIL DEVE CONTER\033[m \033[32m"@"\033[m')
            contar_erros_email += 1
        if emai.count('@') > 1:
            erros_email.append(f'{cor_texto['vermelho']}ERRO, DEVE CONTER APENAS UM\033[m \033[32m"@"\033[m')
            contar_erros_email += 1
        if '..' in emai:
            erros_email.append(f'{cor_texto['vermelho']}ERRO, NÃO É PERMITIDO PONTOS CONSECUTIVOS!\033[m')
            contar_erros_email += 1
        if not '.' in emai:
            erros_email.append(f'{cor_texto['vermelho']}O EMAIL DEVE CONTER PONTO "."\033[m')
            contar_erros_email += 1
        if '@' in emai:
            local , dominio_parte = emai.split('@', 1)
            if local.startswith('.') or local.endswith('.'):
                erros_email.append(f'{cor_texto['vermelho']}ERRO, PARTE\033[m \033[32m"@"\033[m \033[31mNÃO PODE COMEÇAR NEM TERMINAR COM PONTO: "."\033[m')
                contar_erros_email += 1
            if dominio_parte.startswith('.') or dominio_parte.endswith('.'):
                erros_email.append(f'{cor_texto['vermelho']}DOMÍNIO DEPOIS\033[m \033[32m"@"\033[m \033[31mNÃO PODE COMEÇAR/TERMINAR COM PONTO: "."\033[m')
                contar_erros_email += 1
            if '..' in emai:
                erros_email.append(f'{cor_texto['vermelho']}NÃO PODE CONTER PONTOS CONSECUTIVOS: ".."\033[m')
        if erros_email:                                                                                                 # Condição para exibição dos erros.
            if contar_erros_email == 1:
                print(f'{cor_texto['cinza']}---->VALIDANDO...\033[m')
                print(f'{cor_texto['vermelho']}{contar_erros_email}\033[m \033[37mERRO ENCONTRADO!\033[m\n')
                for erro in erros_email:
                    sleep(0.5)
                    print(erro)
                print(f'{cor_texto['verde']}### TENTE NOVAMENTE ###\033[m\n')
            else:
                sleep(0.5)
                print(f'{cor_texto['cinza']}---->VALIDANDO...\033[m')
                sleep(0.5)
                print(f'{cor_texto['vermelho']}{contar_erros_email}\033[m \033[37mERROS ENCONTRADOS!\033[m\n')
                for erro in erros_email:
                    sleep(0.5)
                    print(erro)
                print(f'{cor_texto['verde']}{texto_formato['grifado']}### TENTE NOVAMENTE ###\033[m\n')
        else:
            print(f'{cor_texto['verde']}{texto_formato['sublinhado']}EMAIL CRIADO COM SUCESSO!\033[m')
            return emai

# ÁREA ONDE O USUÁRIO VAI CRIAR SEU ENDEREÇO ELETRÔNICO E SENHA, OBEDECENDO TODAS AS CONDIÇÕES DAS SUAS RESPECTIVAS FUNÇÕES.
print(f'{cor_texto['amarelo']}{texto_formato['sublinhado']}----- ÁREA DE CRIAÇÃO DE LOGIN -----\033[m')
# A senha e email são guardados dentro de seu respectivo vetor (lista), de modo a ser resgatada pelo código de resgate.
email_resgate = []
senha_resgatar = []
print()
criar_meu_email = validar_emaill(f'{texto_formato['invertido']} CRIE UM EMAIL:\033[m ')
email_resgate.append(criar_meu_email)
print()
criar_minha_senha = validar_senha(f'{texto_formato['invertido']} CRIE UMA SENHA:\033[m ')
senha_resgatar.append(criar_minha_senha)
print()
codigo_de_resgate = validar_codigo(f'{texto_formato['invertido']} CRIE UM CÓDIGO DE RESGATE:\033[m ')
print()

#ÁREA ONDE SERÁ FEITA A VALIDÇÃO DOS DADOS CADASTRAIS.
#NÃO SERÁ NECESSARIO TRATAR ERROS DE CRITÉRIOS, APENAS DE VALIDAÇÃO ENTRE O QUE FOI CRIADO E ACESSADO, POIS ELES FORAM TRATADOS DURANTE O USO DA FUNÇÃO.

print(f'{cor_texto['amarelo']}{texto_formato['sublinhado']}----- ÁREA DE ACESSO AO LOGIN -----\033[m')
print()
while True:                                                                                                             # Todas as condições estarão dentro do while True, ou seja, elas serão testadas até o usuário acertar.
    acessar_meu_email = input(f'{texto_formato['invertido']} INFORME SEU ENDEREÇO DE EMAIL:\033[m ').strip().lower()            # variável de acesso ao email já criado.
    print()
    acessar_minha_senha = input(f'{texto_formato['invertido']} INFORME SUA SENHA:\033[m ').strip()                      # variável de acesso à senha já criado.
    if acessar_minha_senha == criar_minha_senha and acessar_meu_email == criar_meu_email:                               # Condição para validar email e senha, a fim de liberar acesso e quebrar o resto do código (break).
        sleep(0.5)
        print(f'{cor_texto['cinza']}---->VALIDANDO DADOS...\033[m')
        print()
        sleep(0.5)
        print(f'{cor_texto['cinza']}CRIANDO CONTA EM:\033[m\n')
        for i in range(3, 0, -1):
            print(f'{i}°')
            sleep(1)
        print(f'{cor_texto['verde']}@@@ LOGIN ACESSADO COM SUCESSO! @@@')
        break
    if acessar_minha_senha != criar_minha_senha and acessar_meu_email != criar_meu_email:                               # Condição para ignorar o bloco abaixo e voltar ao início, pois não é possível usar o código de resgate aqui.
        sleep(0.3)
        print(f'{cor_texto['cinza']}---->VALIDANDO DADOS...\033[m')
        sleep(0.3)
        print()
        print(f'{texto_formato['invertido']}{cor_texto['branco']}{cor_fundo['vermelho']} O EMAIL E SENHA INSERIDOS NÃO EXISTEM, POR FAVOR INSIRA OS DADOS CORRETAMENTE! \033[m\n')
        continue
    if acessar_minha_senha == criar_minha_senha and acessar_meu_email != criar_meu_email:                               # Condição para uso do código de resgate para resgatar email criado.
        sleep(0.5)
        print(f'{cor_texto['vermelho']}ACESSO NEGADO, EMAIL INCORRETO.\033[m\n')
        contar_erro_codigo1 = 3
        for i in range(1, contar_erro_codigo1 + 1):
            sleep(0.3)
            print(f'{cor_texto['azul']}Resgate seu email com o código de resgate, para acessar conta:\033[m\n')
            sleep(0.3)
            resgatar_email = validar_codigo(f'{texto_formato['invertido']} DIGITE SEU CÓDIGO DE RESGATE:\033[m ')                                               # Variável para digitar o código de resgate e validar.
            if resgatar_email == codigo_de_resgate:                                                                     # Tratando código inválido com for.
                sleep(0.3)
                print(f'{cor_texto['verde']}SEU EMAIL É:\033[m {cor_texto["roxo"]}{email_resgate}\033[m')
                print()
                break
            else:
                if i < 3:
                    sleep(0.3)
                    print(f'{cor_texto['vermelho']}CÓDIGO INVÁLIDO, TENTE NOVAMENTE! TENTATIVA N°{i}\033[m')
                    print()
                elif i == 3:
                    print(f'{cor_texto['vermelho']}TENTATIVAS ESGOTADAS, REFAÇA O PROCESSO DE LOGIN!\033[m')
    elif acessar_minha_senha != criar_minha_senha and acessar_meu_email == criar_meu_email:                             # Condição para tratar senha errada, através do código também.
        sleep(0.3)
        contar_erro_codigo2 = 3
        print(f'{cor_texto['vermelho']}ACESSO NEGADO, SENHA INCORRETA.\033[m\n')
        for i in range(1, contar_erro_codigo2 + 1):
            sleep(0.3)
            print(f'{cor_texto['azul']}Resgate sua senha com o código de resgate, para acessar conta:\033[m\n')
            sleep(0.3)
            resgatar_senha = validar_codigo(f'{texto_formato['invertido']} DIGITE SEU CÓDIGO DE RESGATE:\033[m ')                                               # Variável para digitar o código de resgate e validar.
            print()
            if resgatar_senha == codigo_de_resgate:                                                                     # Tratndo erro no código de resgate para senha.
                sleep(0.3)
                print(f'{cor_texto['verde']}SUA SENHA É:\033[m {cor_texto["roxo"]}{senha_resgatar}\033[m')
                print()
                break
            else:
                if i < 3:
                    sleep(0.3)
                    print(f'{cor_texto['vermelho']}CÓDIGO INVÁLIDO, TENTE NOVAMENTE! TENTATIVA N°{i}\033[m')
                elif i == 3:
                    print(f'{cor_texto['vermelho']}TENTATIVAS ESGOTADAS, REFAÇA O PROCESSO DE LOGIN!\033[m')
