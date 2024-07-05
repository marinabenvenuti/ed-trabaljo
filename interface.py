class Interface():
    def __init__(self) -> None:
        pass

    def tela_inicial(self):
        print()
        print('Bem vindo à livraria :)')
        print()
        print('Escolha uma opção abaixo: ')
        print('1 - Inclusão de livro')
        print('2 - Busca de livro')
        print('3 - Exclusão de livro')
        print('4 - Exibir livros')
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