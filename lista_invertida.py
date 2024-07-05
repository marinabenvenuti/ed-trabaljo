import random
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
                self.__interface.print_basico(inclusao)
            
            elif opcao == '2':
                self.busca_geral()

            elif opcao == '3':
                if self.__livros == []:
                    self.__interface.print_basico('Sem livros cadastrados')
                else:
                    self.excluir_livro()

            elif opcao == '4':
                if self.__livros == []:
                    self.__interface.print_basico('Sem livros cadastrados')
                else:
                    self.__interface.exibir_livros(self.__livros)

            elif opcao == '5':
                self.carga_de_dados()

            elif opcao == '0':
                exec = False

    def intervalo_preco(self, livro):
        if livro.preco < 30.00:
            self.__precos['30'].append(livro.id)
        
        elif livro.preco > 30.00 and livro.preco < 50.00:
            self.__precos['50'].append(livro.id)
        
        elif livro.preco > 50.00 and livro.preco < 100.00:
            self.__precos['100'].append(livro.id)
        
        elif livro.preco > 100.00 and livro.preco < 200.00:
            self.__precos['200'].append(livro.id)
        
        elif livro.preco > 200.00:
            self.__precos['acima'].append(livro)

    def gerar_id(self):
        return random.randint(0, 100000)
    
    def incluir_nos_diretorios(self, livro, cod):
        # adicionando autor ou id novo no diretório
        if self.__autores != []:
            cont = 0
            for autor in self.__autores:
                if autor.item == livro.autor:
                    autor.add_id(cod)
                    cont += 1
            if cont == 0:
                autor = ItemDiscretoDiretorio(livro.autor, cod)
                self.__autores.append(autor)
        else:
            autor = ItemDiscretoDiretorio(livro.autor, cod)
            self.__autores.append(autor)

        # adicionando genero ou id novo no diretório
        if self.__generos != []:
            cont = 0
            for genero in self.__generos:
                if genero.item == livro.genero:
                    genero.add_id(cod)
                    cont += 1
            if cont == 0:
                genero = ItemDiscretoDiretorio(livro.genero, cod)
                self.__generos.append(genero)
        else:
            genero = ItemDiscretoDiretorio(livro.genero, cod)
            self.__generos.append(genero)

        # adicionando preço
        self.intervalo_preco(livro)


    def incluir_livro(self):
        infos_livro = self.__interface.incluir_livro()

        for livro in self.__livros:
            if infos_livro[0] == livro.nome and infos_livro[1] == livro.autor and infos_livro[2] == livro.genero:
                return 'Este livro já está cadastrado!'
            
        cod = self.gerar_id()
        livro = Livro(cod, infos_livro[0], infos_livro[1], infos_livro[2], infos_livro[3])
        self.__livros.append(livro)

        self.incluir_nos_diretorios(livro, cod)
    
        return f'Livro {livro.nome} adicionado ao sistema'
    
    def busca_geral(self):
        while True:
            opcao_busca = self.__interface.opcoes_busca()

            if opcao_busca == '1':
                nome = self.__interface.busca_basica('nome')
                encontrados = [livro for livro in self.__livros if livro.nome == nome]
                if encontrados:
                    for livro in encontrados:
                        self.__interface.print_livro(livro)
                else:
                    self.__interface.print_basico('Livro não encontrado')

            elif opcao_busca == '2':
                result = self.busca_autor()
                if result == 'Autor não encontrado':
                    self.__interface.print_basico('Autor não encontrado')
                else:
                    self.__interface.print_basico('Livros com o autor informado:')
                    self.livro_por_id(result)

            elif opcao_busca == '3':
                result = self.busca_genero()
                if result == 'Gênero não encontrado':
                    self.__interface.print_basico('Gênero não encontrado')
                else:
                    self.__interface.print_basico('Livros com o gênero informado:')
                    self.livro_por_id(result)

            elif opcao_busca == '4':
                result = self.busca_preco()
                if result == []:
                    self.__interface.print_basico('Sem livros neste intervalo')
                else:
                    self.__interface.print_basico('Livros com o intervalo de preço informado: ')
                    self.livro_por_id(result)

            elif opcao_busca == '5':
                result_autor = self.busca_autor()
                result_genero = self.busca_genero()
                if result_autor == 'Autor não encontrado' or result_genero == 'Gênero não encontrado':
                    self.__interface.print_basico('O gênero e/ou o autor informado não está cadastrado. Tente novamente')
                else:
                    self.__interface.print_basico('Livro(s) com o autor e gênero informado')
                    encontrados = [livro for livro in self.__livros if livro.id in result_autor and livro.id in result_genero]
                    if encontrados:
                        for livro in encontrados:
                            self.__interface.print_livro(livro)
                    else:
                        self.__interface.print_basico('Nenhum livro encontrado com o autor e gênero informado')

            elif opcao_busca == '6':
                result_autor = self.busca_autor()
                result_preco = self.busca_preco()
                if result_autor == 'Autor não encontrado' or result_preco == []:
                    self.__interface.print_basico('O autor e/ou o intervalo de preço informado não está cadastrado. Tente novamente')
                else:
                    self.__interface.print_basico('Livro(s) com o autor e intervalo de preço informado')
                    for livro in self.__livros:
                        for id_a in result_autor:
                            for id_p in result_preco:
                                if livro.id==id_a and livro.id==id_p:
                                    self.__interface.print_livro(livro)

            elif opcao_busca == '7':
                result_genero = self.busca_genero()
                result_preco = self.busca_preco()
                if result_genero == 'Gênero não encontrado' or result_preco == []:
                    self.__interface.print_basico('O gênero e/ou o intervalo de preço informado não está cadastrado. Tente novamente')
                else:
                    self.__interface.print_basico('Livro(s) com o gênero e intervalo de preço informado')
                    for livro in self.__livros:
                        for id_g in result_genero:
                            for id_p in result_preco:
                                if livro.id==id_g and livro.id==id_p:
                                    self.__interface.print_livro(livro)
                    

            elif opcao_busca == '0':
                break

    def livro_por_id(self, result):
        for livro in self.__livros:
            for id in result:
                if livro.id == id:
                    self.__interface.print_livro(livro)
    
    def busca_autor(self):
        autor = self.__interface.busca_basica('autor')
        for autores in self.__autores:
            if autor == autores.item:
                return autores.ids
        return 'Autor não encontrado'
        

    def busca_genero(self):
        genero = self.__interface.busca_basica('gênero')
        for generos in self.__generos:
            if genero == generos.item:
                print(generos.ids)
                return generos.ids
        return 'Gênero não encontrado'

    def busca_preco(self):
        preco = self.__interface.opcoes_preco()
        if preco == '1':
            return self.__precos['30']
        if preco == '2':
            return self.__precos['50']
        if preco == '3':
            return self.__precos['100']
        if preco == '4':
            return self.__precos['200']
        if preco == '5':
            return self.__precos['acima']
        
    def excluir_livro(self):
        opcao_exclusao = self.__interface.opcoes_exclusao()
        if opcao_exclusao == '1':
            id_livro = self.__interface.obter_id_livro()
            livro_para_excluir = None
            for livro in self.__livros:
                if livro.id == id_livro:
                    livro_para_excluir = livro
                    break
            if livro_para_excluir:
                self.__livros.remove(livro_para_excluir)
                self.atualizar_estruturas_apos_exclusao(livro_para_excluir)
                self.__interface.print_basico(f'Livro {livro_para_excluir.nome} excluído com sucesso')
            else:
                self.__interface.print_basico('Livro não encontrado')
        elif opcao_exclusao == '2':
            nome_livro = self.__interface.obter_nome_livro()
            livros_para_excluir = [livro for livro in self.__livros if livro.nome == nome_livro]
            if livros_para_excluir:
                for livro in livros_para_excluir:
                    self.__livros.remove(livro)
                    self.atualizar_estruturas_apos_exclusao(livro)
                self.__interface.print_basico(f'{len(livros_para_excluir)} livro(s) com nome "{nome_livro}" excluído(s) com sucesso')
            else:
                self.__interface.print_basico('Livro não encontrado')

    def atualizar_estruturas_apos_exclusao(self, livro):
        for autor in self.__autores:
            if livro.id in autor.ids:
                autor.ids.remove(livro.id)
                if not autor.ids:
                    self.__autores.remove(autor)

        for genero in self.__generos:
            if livro.id in genero.ids:
                genero.ids.remove(livro.id)
                if not genero.ids:
                    self.__generos.remove(genero)

        for intervalo, ids in self.__precos.items():
            if livro.id in ids:
                ids.remove(livro.id)
        
    def carga_de_dados(self):
        livros_exemplo = [
            ("Dom Casmurro", "Machado de Assis", "Romance", 40.00),
            ("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance", 50.00),
            ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 35.00),
            ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 80.00),
            ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 45.00),
            ("1984", "George Orwell", "Ficção Científica", 30.00),
            ("Orgulho e Preconceito", "Jane Austen", "Romance", 40.00),
            ("A Revolução dos Bichos", "George Orwell", "Fábula", 35.00),
            ("Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico", 55.00),
            ("Crime e Castigo", "Fiódor Dostoiévski", "Romance", 60.00),
        ]

        for infos_livro in livros_exemplo:
            id_aleatorio = self.gerar_id()
            livro = Livro(id_aleatorio, infos_livro[0], infos_livro[1], infos_livro[2], infos_livro[3])
            self.__livros.append(livro)

            self.incluir_nos_diretorios(livro, id_aleatorio)
        
        self.__interface.print_basico("Carga de dados concluída! 10 livros adicionados ao sistema.")
