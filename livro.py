class Livro():
    def __init__(self, id, nome, autor, genero, preco):
        self.__id = id
        self.__nome = nome
        self.__autor = autor
        self.__genero = genero
        self.__preco = preco

    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def preco(self):
        return self.__preco
    