# Importa as classes a serem instanciadas para auxiliar no código
from livro import Livro
from usuario import Usuario

# Classe onde foi desenvolvida a lógica do sistema
from sistema import SistemaBiblioteca

# Cria uma instância do sistema gerenciador de bibliotecas para a 'Biblioteca do Bairro'
bibliotecaDoBairro = SistemaBiblioteca()

# (OPCIONAL) Cria instâncias de livros e usuários para facilitar o uso do sistema
livros = [
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 0),
    Livro("O Senhor dos Anéis II", "J.R.R. Tolkien", 1997, 5),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 6),
    Livro("Harry Potter e a Ordem da Fênix", "J.K. Rowling", 2003, 3),
    Livro("O Código Da Vinci", "Dan Brown", 2003, 7),
    Livro("1984", "George Orwell", 1949, 2),
    Livro("Dom Quixote", "Miguel de Cervantes", 1605, 3)
]
usuarios = [
    Usuario('João Silva', 111, 111111),
    Usuario('João Pedro', 222, 123456),
    Usuario('Maria Silva', 333, 654321),
    Usuario('Aline Santos', 444, 112233),
    Usuario('Joaldo Teixeira', 123, 332211),
]
# (OPCIONAL) Popula o sistema da biblioteca com valores iniciais
bibliotecaDoBairro.livros = livros
bibliotecaDoBairro.usuarios = usuarios

# Método chamado para iniciar o sistema
bibliotecaDoBairro.menuPrincipal()