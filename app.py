# sistema de login simples
resposta = input('[1] - Cadastrar novo usuário\n[2] - Fazer login: ')
usuarios = ['carol', 'amanda', 'jeff']
senhas = ['123456', 'abcdef', '123abcd']
if resposta == '1':
    # cadastrar os usuários

    usuario_digitado = input('Digite seu usuário: ')
    # não permitir duplicados
    if usuario_digitado in usuarios:
        print('usuário existente')

    else:
        senha_digitada = input('Digite sua senha: ')

    usuarios.append(usuario_digitado)
    senhas.append(senha_digitada)

    print('Usuário cadastrado! Agora você pode fazer login! ')
    usuario_digitado = input('Digite seu usuário: ')

    senha_digitada = input('Digite sua senha: ')
    # verificar se usuario existe na lista
    ecnontrado = False
    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario:
            if senha_digitada == senhas[indice]:
                print('Login feito com sucesso')
                encontrado = True
            elif encontrado == False:
                print('usuário ou senha incorreto!')
elif resposta == '2':
    # permitir fazer login

    usuario_digitado = input('Digite seu usuário: ')

    senha_digitada = input('Digite sua senha: ')
    # verificar se usuario existe na lista
    ecnontrado = False

    for indice, usuario in enumerate(usuarios):
        if usuario_digitado == usuario:
            # conferirir senhas
            if senha_digitada == senhas[indice]:
                print('Login feito com sucesso')
                encontrado = True
    # alertar se as informações não estiverem corretos
            elif encontrado == False:
                print('usuário ou senha incorreto!')
    if usuario_digitado not in usuarios:
        print('usuário ou senha incorreto!')


else:
    print('Digite apenas 1 ou 2')
