# Lista Invertida
Este projeto foi desenvolvido na disciplina de Estrutura de Dados e trata da implementação de uma livraria onde os dados são organizados através de uma lista invertida. A tarefa oferecia a opção de implementar uma multilista ou uma lista invertida. Optou-se pela lista invertida devido ao seu melhor desempenho em buscas compostas.

# Estrutura do código
O projeto foi dividido em 4 classes principais, sendo elas: 
* Classe `Livro` e `ItemDiscretoDiretorio`: Estas classes se referem às entidades do projeto. A classe `Livro` representa cada livro na livraria, contendo informações como nome, autor, gênero e preço. A classe `ItemDiscretoDiretorio` representa um item do diretório de autores e gêneros, armazenando um item (autor ou gênero) e os IDs dos livros associados a ele.
* Classe `ListaInvertida`: Esta classe armazena a lista invertida em si, que seria o atributo `__livros`, os diretórios e toda a lógica do programa. A lista invertida permite uma organização eficiente dos dados para facilitar as buscas.
* Classe `Interface`: Esta classe faz toda a comunicação com o usuário, exibindo e solicitando todos os dados. É responsável pela interação do sistema com o usuário, permitindo a inclusão, busca, exclusão e exibição de livros.

### Justificativa das decisões:
* Dicionário no diretório de preço: Utilizou-se um dicionário para os preços, categorizando-os em intervalos específicos. Isso facilita a busca por intervalo de preço, pois permite acessar diretamente os livros que pertencem a cada faixa de preço.
* Objetos nos diretórios de autor e gênero: Utilizou-se objetos da classe `ItemDiscretoDiretorio` para representar cada autor e gênero, armazenando o item (autor ou gênero) e uma lista de IDs dos livros associados. Essa abordagem facilita a manutenção e a busca, permitindo associar facilmente múltiplos livros a um autor ou gênero.
* Objetos em cada item livro da lista invertida: Cada livro é representado por um objeto da classe `Livro`, que encapsula todas as informações relevantes sobre o livro. Isso permite um gerenciamento mais estruturado e orientado a objetos dos dados, facilitando a manutenção e a extensão do sistema.

# Funcionamento
Os métodos da lista invertida implementada podem ser separados em 5, sendo eles:

## Método de adição
O método `incluir_livro` permite a adição de um novo livro ao sistema. Ele verifica se o livro já está cadastrado, gera um ID único para o novo livro e adiciona o livro aos diretórios de autores, gêneros e preços, além de adicioná-lo à lista de livros.

## Método de busca
O método `busca_geral` oferece várias opções de busca, permitindo buscar livros por nome, autor, gênero, intervalo de preço, autor e gênero, autor e intervalo de preço ou gênero e intervalo de preço. Para cada opção de busca, o sistema interage com o usuário para obter os critérios de busca e exibe os resultados encontrados.

## Método de remoção
O método `excluir_livro` permite a exclusão de um livro do sistema, seja pelo ID ou pelo nome do livro. Ele remove o livro da lista de livros e atualiza as estruturas de dados (diretórios de autores, gêneros e preços) para refletir a exclusão.

## Método de exibição
O método `exibir_livros` exibe todos os livros cadastrados no sistema. Ele interage com a classe `Interface` para mostrar as informações dos livros de forma clara para o usuário.

## Método de carga de dados
O método `carga_de_dados carrega um conjunto de livros de exemplo no sistema. Esse método é útil para testes e demonstrações, permitindo adicionar rapidamente um conjunto de livros predefinidos.

# Autores: Marina Benvenuti e Yano Cavalcante
