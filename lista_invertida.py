from interface import Interface
from livro import Livro
from item_discreto_diretorio import ItemDiscretoDiretorio

class ListaInvertida():
    def __init__(self):
        self.__autores = []
        self.__generos = []
        self.__precos = {'30': [], '50': [], '100': [], '200': [], 'acima': []}
        self.__livros = []
        self.__interface = Interface()

    def inicializa_sistema(self):
        exec = True
        while exec:
            opcao = self.__interface.tela_inicial()

            if opcao == '1':
                inclusao = self.incluir_livro()
                print(inclusao)
            
            elif opcao == '2':
                pass

            elif opcao == '3':
                pass

            elif opcao == '4':
                pass

            elif opcao == '5':
                pass

            elif opcao == '0':
                exec = False

    def intervalo_preco(self, livro):
        if livro.preco < 30.00:
            self.__precos['30'].append(livro)
        
        elif livro.preco > 30.00 and livro.preco < 50.00:
            self.__precos['50'].append(livro)
        
        elif livro.preco > 50.00 and livro.preco < 100.00:
            self.__precos['100'].append(livro)
        
        elif livro.preco > 100.00 and livro.preco < 200.00:
            self.__precos['200'].append(livro)
        
        elif livro.preco > 200.00:
            self.__precos['acima'].append(livro)

    def incluir_livro(self):
        infos_livro = self.__interface.incluir_livro()

        for livro in self.__livros:
            if infos_livro[0] == livro.nome and infos_livro[1] == livro.autor and infos_livro[2] == livro.genero:
                return('Este livro já está cadastrado!')
            
        livro = Livro(0, infos_livro[0], infos_livro[1], infos_livro[2], infos_livro[3])
        self.__livros.append(livro)

        # adicionando autor ou id novo no diretório
        if self.__autores != []:
            cont = 0
            for autor in self.__autores:
                if autor.item == livro.autor:
                    autor.add_id(0)
                    cont += 1
            if cont == 0:
                autor = ItemDiscretoDiretorio(livro.autor, 0)
                self.__autores.append(autor)
        else:
            autor = ItemDiscretoDiretorio(livro.autor, 0)
            self.__autores.append(autor)

        # adicionando genero ou id novo no diretório
        if self.__generos != []:
            cont = 0
            for genero in self.__generos:
                if genero.item == livro.genero:
                    genero.add_id(0)
                    cont += 1
            if cont == 0:
                genero = ItemDiscretoDiretorio(livro.genero, 0)
                self.__generos.append(genero)
        else:
            genero = ItemDiscretoDiretorio(livro.genero, 0)
            self.__generos.append(genero)

        # adicionando preço
        self.intervalo_preco(livro)
    
        return f'Livro {livro.nome} adicionado ao sistema'
    
