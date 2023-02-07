from os import system
import time

class Musica:
    def __init__ (self, id, nome, album, banda):
        self.id = id
        self.nome = nome
        self.album = album
        self.banda = banda
        self.idPlaylist = 0
    
    def __str__ (self):
        possuiPlaylist = 'Não possui playlist!'
        if (self.idPlaylist != 0): possuiPlaylist = 'Possui playlist!'
        
        return f'{self.nome} - {self.banda} | {self.album} | {possuiPlaylist}'

# -------------------------------------------------------------------------------------------------------------

class NMusica:
    musicas = []
    
    @classmethod
    def inserir (cls, musica):
        cls.musicas.append(musica)
    
    @classmethod
    def listar (cls):
        return cls.musicas
        
    @classmethod
    def excluir (cls, m):
        removeu = False
        for musica in cls.musicas:
            if (m.id == musica.id):
                cls.musicas.remove(m)
                removeu = True
        
        return removeu
    
    @classmethod
    def countMusicas (cls, id):
        numMusicas = 0
        for musica in cls.musicas:
            if (musica.idPlaylist == id): numMusicas += 1
        
        return numMusicas

# -------------------------------------------------------------------------------------------------------------

class listPlaylistItems:
    musicas_playlist = []
    
    @classmethod
    def addMusPlay (cls, musica, playlist):
        musica.idPlaylist = playlist.id
        cls.musicas_playlist.append(musica)
    
    @classmethod
    def removeMusPlay (cls, musica):
        musica.idPlaylist = 0
        cls.musicas_playlist.remove(musica)
    
    @classmethod
    def removerMusicas (cls, playlist):
        playlists = NPlaylist.listar()
        for i in range(len(playlists)):
            if (cls.musicas_playlist[i].idPlaylist == playlist.id):
                cls.musicas_playlist.remove(cls.musicas_playlist[i])

# -------------------------------------------------------------------------------------------------------------

class Playlist:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome
        self.idUsuario = 0
        
    def __str__ (self):
        return f'{self.nome} | Musicas: {NMusica.countMusicas(id)}'
        
# -------------------------------------------------------------------------------------------------------------

class NPlaylist:
    playlists = []
    
    @classmethod
    def inserir (cls, playlist):
        cls.playlists.append(playlist)
    
    @classmethod
    def listar (cls):
        return cls.playlists
        
    @classmethod
    def excluir (cls, p):
        removeu = False
        for playlist in cls.playlists:
            if (p.id == playlist.id):
                cls.playlists.remove(p)
                removeu = True
        
        return removeu
    
    @classmethod
    def countPlaylists (cls, id):
        numPlaylists = 0
        for playlist in cls.playlists:
            if (playlist.idUsuario == id): numPlaylists += 1
        
        return numPlaylists

# -------------------------------------------------------------------------------------------------------------
   
class Usuario:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome
        self.idUsuario = 0
        
    def __str__ (self):
        return f'{self.nome} | Playlists: {NPlaylist.countPlaylists(self.id)}'

# -------------------------------------------------------------------------------------------------------------

class NUsuario:
    usuarios = []
    
    @classmethod
    def inserir (cls, usuario):
        cls.usuarios.append(usuario)
    
    @classmethod
    def listar (cls):
        return cls.usuarios
        
    @classmethod
    def excluir (cls, u):
        removeu = False
        for usuario in cls.usuarios:
            if (u.id == usuario.id):
                cls.usuarios.remove(u)
                removeu = True
        
        return removeu
    
    @classmethod
    def countUsuarios (cls, id):
        return len(cls.usuarios)

# -------------------------------------------------------------------------------------------------------------

class Admin (Usuario):
    def __init__ (self, id, nome):
        super().init(id, nome)

# -------------------------------------------------------------------------------------------------------------

class Menu:
    def __init__ (self):
        pass
    
    def exibir (self):
        system('cls')
        print('''
Bom dia! Bem vindo ao Rockify.
Escolha uma opção abaixo:
1 - Adicionar musica no app
2 - Remover musica do app
3 - Listar musicas do app
4 - Adicionar playlist no app
5 - Remover playlist do app
6 - Listar playlists do app
7 - Adicionar usuario no app
8 - Remover usuario do app
9 - Listar usuarios do app
10 - Adicionar musica em uma playlist
11 - Remover musica de uma playlist
0 - Sair
        ''')
        return int(input())
    
    def addMusica (self):
        system('cls')
        print('Digite, respectivamente: id, nome, album e banda da musica: ')
        m = Musica(int(input()), input(), input(), input())
        NMusica.inserir(m)
        print('Musica inserida com sucesso!')
        
    def removeMusica (self):
        system('cls')
        print('Escolha uma musica para remover: ')
        musicas = NMusica.listar()
        for i in range(len(musicas)):
            print(f'{i+1} - {musicas[i]}')
        opc = int(input())
        removeu = NMusica.excluir(musicas[opc-1])
        if (removeu):
            print('Musica removida com sucesso!')
        else:
            print('ERRO: Musica não removida')
        
    def listMusica (self):
        system('cls')
        print('Lista de musicas: ')
        musicas = NMusica.listar()
        for i in range(len(musicas)):
            print(f'{i+1} - {musicas[i]}')
        input()
        
    def addPlaylist (self):
        system('cls')
        print('Digite, respectivamente: id e nome da playlist: ')
        p = Playlist(int(input()), input())
        NPlaylist.inserir(p)
        print('Playlist inserida com sucesso!')
        
    def removePlaylist (self):
        system('cls')
        print('Escolha uma playlist para remover: ')
        playlists = NPlaylist.listar()
        for i in range(len(playlists)):
            print(f'{i+1} - {playlists[i]}')
        opc = int(input())
        removeu = NPlaylist.excluir(playlists[opc-1])
        if (removeu):
            print('Playlist removida com sucesso!')
        else:
            print('ERRO: Playlist não removida')
        
    def listPlaylist (self):
        system('cls')
        print('Lista de playlists: ')
        playlists = NPlaylist.listar()
        for i in range(len(playlists)):
            print(f'{i+1} - {playlists[i]}')
        input()
            
    def addUsuario (self):
        print('Digite, respectivamente: id e nome do usuario: ')
        u = Usuario(int(input()), input())
        NUsuario.inserir(u)
        print('Usuario inserido com sucesso!')
        
    def removeUsuario (self):
        system('cls')
        print('Escolha um usuario para remover: ')
        usuarios = NUsuario.listar()
        for i in range(len(usuarios)):
            print(f'{i+1} - {usuarios[i]}')
        opc = int(input())
        removeu = NUsuario.excluir(usuarios[opc-1])
        if (removeu):
            print('Usuario removido com sucesso!')
        else:
            print('ERRO: Usuario não removido')
        
    def listUsuario (self):
        system('cls')
        print('Lista de usuarios: ')
        usuarios = NUsuario.listar()
        for i in range(len(usuarios)):
            print(f'{i+1} - {usuarios[i]}')
        input()
            
    def addMusicaPlay (self):
        system('cls')
        musicas = NMusica.listar()
        playlists = NPlaylist.listar()
        self.listMusica()
        opc = int(input('Escolha uma musica acima: '))
        system('cls')
        self.listPlaylist()
        opc2 = int(input('Escolha uma playlist acima: '))
        listPlaylistItems.addMusPlay(musicas[opc-1], playlists[opc2-1])
        print(f'{musicas[opc-1].nome} foi adicionada com sucesso a {playlists[opc2-1].nome}!')
        
    def removeMusicaPlay (self):
        musicas = NMusica.listar()
        self.listMusica()
        opc = int(input('Escolha uma musica acima: '))
        listPlaylistItems.removeMusPlay(musicas[opc-1])
        print(f'{musicas[opc-1].nome} foi removida com sucesso das playlists correspondentes!')
