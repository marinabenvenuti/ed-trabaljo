class Interface():
    def __init__(self) -> None:
        pass

    def tela_inicial(self):
        print()
        print('Bem vindo à livraria :)')
        print('---------------------------------------')
        print('Escolha uma opção abaixo: ')
        print('---------------------------------------')
        print('1 - Inclusão de livro')
        print('2 - Busca de livro')
        print('3 - Exclusão de livro')
        print('4 - Exibir todos os livros')
        print('5 - Carga de dados')
        print('0 - Finalizar sistema')
        print()
        opcao = input('Escolha uma opção: ')
        return opcao
    
    def incluir_livro(self):
        nome = input('Digite o nome do livro: ')
        autor = input('Digite o autor(a) do livro: ')
        genero = input('Digite o gênero do livro: ')
        preco = float(input('Digite o preço do livro: '))
        print()

        return nome, autor, genero, preco
    
    def opcoes_busca(self):
        print()
        print('Escolha uma opção de busca: ')
        print('----------------------------------')
        print('1 - Buscar por nome')
        print('2 - Buscar por autor')
        print('3 - Buscar por gênero')
        print('4 - Buscar por intervalo de preço')
        print('5 - Buscar por autor e gênero')
        print('6 - Buscar por autor e intervalo de preço')
        print('7 - Buscar por gênero e intervalo de preço')
        print('0 - Voltar')
        print()
        opcao = input('Digite a opção: ')
        return opcao
    
    def opcoes_preco(self):
        print()
        print('Escolha um intervalo de preço')
        print('------------------------------------')
        print('1 - Até R$30,00')
        print('2 - Entre R$30 e R$50')
        print('3 - Entre R$50 e R$100')
        print('4 - Entre R$100 e R$200')
        print('5 - Acima de R$200')
        print()
        intervalo = input('Escolha um intervalo: ')
        return intervalo
    
    def busca_basica(self, tipo):
        tipo = input(f'Digite o {tipo} do livro: ')
        return tipo
    
    def print_livro(self, livro):
        print()
        print(f'Livro: {livro.nome}')
        print(f'Autor: {livro.autor}')
        print(f'Gênero: {livro.genero}')
        print(f'Preço: {livro.preco}')
        print('-------------------------------------')

    def print_basico(self, conteudo):
        print()
        print(conteudo)
        print()

    def exibir_livros(self, livros):
        if not livros:
            print("Não há livros cadastrados.")
        else:
            print("{:<5} {:<25} {:<25} {:<15} {:<10}".format("ID", "Nome", "Autor", "Gênero", "Preço"))
            print("="*80)
            for livro in livros:
                print("{:<5} {:<25} {:<25} {:<15} R${:<10.2f}".format(livro.id, livro.nome, livro.autor, livro.genero, livro.preco))
            print("="*80)
    
    def opcoes_exclusao(self):
        print("Opções de exclusão")
        print("1 - Excluir por ID")
        print("2 - Excluir por nome")
        return input("Escolha uma opção de exclusão: ")

    def obter_id_livro(self):
        return int(input("Digite o ID do livro a ser excluído: "))

    def obter_nome_livro(self):
        return input("Digite o nome do livro a ser excluído: ")