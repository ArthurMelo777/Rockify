from classes import *
from os import system

# Usuario e admin padrao para acesso
u = User('user', 'user')
a = Admin('admin', 'admin')

# Listas que servem como DB do sistema e variaveis
musicas = []
bandas = []
albuns = []
users = [u, a]
user_atual = User('', '')
userCadastrado = False
logado = False

# Tela inicial + login ou cadastro
while True:
    system('cls')
    print('''
    Bem vindo ao Rockify, o melhor sistema de música para amantes do Rock
    1 - Fazer login
    2 - Cadastrar
    ''')
    opc = int(input())
    if (opc == 1):
        print('Digite')
        user = User(input('Nome de usuario: '), input('Senha: '))

        for i in range(len(users)):
            if (user.nome == users[i].nome and user.senha == users[i].senha):
                print(f'Bem vindo {user.nome}')
                input('Aperte qqr tecla para continuar')
                user_atual = users[i]
                logado = True
            else:
                print('Nome de usuario ou senha incorretos!')
        
        if (logado): break

    elif (opc == 2):
        print('Digite')
        user = User(input('Nome de usuario: '), input('Senha: '))

        for i in range(len(users)):
            if (user == users[i].nome):
                userCadastrado = True
                break
        
        if (not userCadastrado):
            new_user = user
            print(f'Usuario cadastrado com sucesso, bem vindo {user}')
            input('Aperte qqr tecla para continuar')
            user_atual = new_user
            users.append(new_user)
            logado = True
            break
        else:
            print('Usuario ja cadastrado! Escolha outro.')
            input('Aperte qqr tecla para continuar')
    else:
        print('Opcao incorreta!')
        input('Aperte qqr tecla para continuar')


# Menu de admin
if (user_atual.admin and logado):
    while True:
        system('cls')
        print(f'''
        Menu de Admin - Bem vindo {user_atual.nome}
        Digite:
        1 - Adicionar musica
        2 - Remover musica
        3 - Adiconar album
        4 - Remover album
        5 - Adiconar banda
        6 - Remover banda
        7 - Remover usuario
        8 - Listar musicas
        9 - Listar albuns
        10 - Listar bandas
        11 - Listar usuarios e admins
        0 - Sair
        ''')
        opc = int(input())

        if (opc == 1):
            system('cls')
            m = Musica(input('Digite a data de lançamento da musica: '), input('Digite o nome da musica: '), len(musicas))
            if (user_atual.verificar(m, musicas)): musicas.append(m)
            input('Aperte qqr tecla para continuar')

        elif (opc == 2):
            system('cls')
            print('Escolha qual musica deseja remover: ')
            user_atual.listar(musicas)
            opc2 = int(input())
            musicas.remove(musicas[opc2])
            input('Aperte qqr tecla para continuar')

        elif (opc == 3):
            system('cls')
            a = Album(input('Digite a data de lançamento do album: '), input('Digite o nome do album: '), len(albuns))
            if (user_atual.verificar(a, albuns)): albuns.append(a)
            input('Aperte qqr tecla para continuar')

        elif (opc == 4):
            system('cls')
            print('Escolha qual album deseja remover: ')
            user_atual.listar(albuns)
            opc2 = int(input())
            albuns.remove(albuns[opc2])
            input('Aperte qqr tecla para continuar')

        elif (opc == 5):
            system('cls')
            b = Banda(input('Digite a data de funcaçao da banda: '), input('Digite o nome da banda: '), len(bandas))
            if (user_atual.verificar(b, bandas)): bandas.append(b)
            input('Aperte qqr tecla para continuar')

        elif (opc == 6):
            system('cls')
            print('Escolha qual banda deseja remover: ')
            user_atual.listar(bandas)
            opc2 = int(input())
            bandas.remove(bandas[opc2])
            input('Aperte qqr tecla para continuar')

        elif (opc == 7):
            system('cls')
            print('Escolha qual usuario deseja remover: ')
            user_atual.listar(users) # um admin pode remover outros admins?
            opc2 = int(input())
            users.remove(users[opc2])
            input('Aperte qqr tecla para continuar')

        elif (opc == 8):
            system('cls')
            print('Lista de todas as musicas inseridas no Rockify: ')
            user_atual.listar(musicas)
            input('Aperte qqr tecla para continuar')

        elif (opc == 9):
            system('cls')
            print('Lista de todos os albuns inseridos no Rockify: ')
            user_atual.listar(albuns)
            input('Aperte qqr tecla para continuar')

        elif (opc == 10):
            system('cls')
            print('Lista de todas as bandas inseridas no Rockify: ')
            user_atual.listar(bandas)
            input('Aperte qqr tecla para continuar')

        elif (opc == 11):
            system('cls')
            print('Lista de todos os usuarios inseridos no Rockify: ')
            user_atual.listar(users)
            input('Aperte qqr tecla para continuar')

        elif (opc == 0):
            system('cls')
            print('Logoff realizado, até mais!')
            print('Deseja logar em outra conta? S/N')
            opc2 = input()
            if ((opc2 == 'S') or (opc2 == 's')):
                pass
            elif ((opc2 == 'N') or (opc2 == 'n')):
                break
            else:
                input('Opcao invalida!')
            input('Aperte qqr tecla para continuar')

# Menu de usuario
if ((not user_atual.admin) and logado):
    while True:
        system('cls')
        print(f'''
        Menu - Bem vindo {user_atual.nome}
        Digite:
        1 - Criar playlist
        2 - Excluir playlist
        3 - Adicionar musica na playlist
        4 - Remover musica da playlist
        5 - Listar musicas da playlist
        6 - Listar playlists
        7 - Excluir conta
        0 - Sair
        ''')
        opc = int(input())

        if (opc == 1):
            system('cls')
            p = Playlist(input('Digite o nome da playlist: '))
            user_atual.playlists.append(p)
            input('Aperte qqr tecla para continuar')

        elif (opc == 2):
            system('cls')
            playlists = user_atual.playlists
            user_atual.listar(playlists)
            if (len(playlists) > 0):
                opc2 = int(input())
                playlists.remove(playlists[opc2])
                print('Playlist excluida com sucesso!')
            input('Aperte qqr tecla para continuar')

        elif (opc == 3):
            system('cls')
            print('Escolha uma playlist para adicionar a musica: ')
            playlists = user_atual.playlists
            user_atual.listar(playlists)
            if (len(playlists) > 0):
                opc2 = int(input())
                print(f'Escolha uma musica para adicionar na playlist "{playlists[opc2]}": ')
                user_atual.listar(musicas)
                if (len(musicas) > 0):
                    opc3 = int(input())
                    playlists[opc2].addMusica(musicas[opc3])
                    print('Musica adicionada com sucesso!')
            input('Aperte qqr tecla para continuar')

        elif (opc == 4):
            system('cls')
            print('Escolha uma playlist para remover a musica: ')
            playlists = user_atual.playlists
            user_atual.listar(playlists)
            if (len(playlists) > 0):
                opc2 = int(input())
                print(f'Escolha uma musica para remover da playlist "{playlists[opc2]}": ')
                user_atual.listar(musicas)
                if (len(musicas) > 0):
                    opc3 = int(input())
                    playlists[opc2].delMusica(musicas[opc3])
                    print('Musica removida com sucesso!')
            input('Aperte qqr tecla para continuar')

        elif (opc == 5):
            system('cls')
            print('Escolha uma playlist para listar as musicas: ')
            playlists = user_atual.playlists
            user_atual.listar(playlists)
            if (len(playlists) > 0):
                opc2 = int(input())
                playlists[opc2].listMusicas
            input('Aperte qqr tecla para continuar')

        elif (opc == 6):
            system('cls')
            print('Lista de playlists: ')
            playlists = user_atual.playlists
            user_atual.listar(playlists)
            input('Aperte qqr tecla para continuar')
        
        elif (opc == 7):
            system('cls')
            while True:
                system('cls')
                print('Deseja mesmo excluir sua conta? S/N')
                opc2 = input()
                if ((opc2 == 'S') or (opc2 == 's')):
                    users.remove(user_atual)
                    input('Conta deletada com sucesso!')
                    deletada = True
                    break
                elif ((opc2 == 'N') or (opc2 == 'n')):
                    break
                else:
                    input('Opcao invalida!')
            if (deletada):
                break
            input('Aperte qqr tecla para continuar')

        elif (opc == 0):
            system('cls')
            print('Logoff realizado, até mais!')
            input('Aperte qqr tecla para continuar')
            break