class Musica:
    def __init__ (self, dataLancamento, nome, id):
        self.dataLancamento = dataLancamento
        self.nome = nome
        self.id = id
    
    def __str__ (self):
        return self.nome + ' - lançada em ' + self.dataLancamento

class Album:
    def __init__ (self, dataLancamento, nome, id):
        self.dataLancamento = dataLancamento
        self.nome = nome
        self.id = id
        self.musicas = []
    
    def __str__ (self):
        return self.nome + ' - lançado em ' + self.dataLancamento + ' possui ' + str(len(self.musicas)) + ' musicas'

    def addMusica (self,  m):
        self.musicas.append(m)
    
    def delMusica (self, m):
        self.musicas.remove(m)
    
    def listMusicas (self):
        for i in range(len(self.musicas)):
            print(i + ' - ' + self.musicas[i])

class Banda:
    def __init__ (self, dataFundacao, nome, id):
        self.dataFundacao = dataFundacao
        self.nome = nome
        self.id = id
        self.albuns = []

    def __str__ (self):
        return self.nome + ' - fundada em ' + self.dataFundacao + ' possui ' + str(len(self.albuns)) + ' albuns'

    def addAlbum (self, a):
        self.albuns.append(a)
    
    def delAlbum (self, a):
        self.albuns.remove(a)
    
    def listAlbuns (self):
        for i in range(len(self.albuns)):
            print(i + ' - ' + self.albuns[i])

class Playlist:
    def __init__ (self, nome):
        self.nome = nome
        self.musicas = []
    
    def __str__ (self):
        return self.nome + ' - ' + str(len(self.musicas)) + ' cadastradas'
    
    def addMusica (self, m):
        self.musicas.append(m)
    
    def delMusica (self, m):
        self.musicas.remove(m)
    
    def listMusicas (self):
        for i in range(len(self.musicas)):
            print(i + ' - ' + self.musicas[i])

class User:
    def __init__ (self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.playlists = []
        self.admin = False
    
    def __str__ (self):
        return self.nome + ' - USER'
    
    def verificar (self, x, l):
        for i in range(len(l)):
            if (x == l[i]): return False
            return True
    
    def listar (self, l):
        for i in range(len(l)):
            print(f'{i} - {l[i]}')

class Admin (User):
    def __init__ (self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.admin = True
    
    def __str__ (self):
        return self.nome + ' - ADMIN'