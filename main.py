# Importa as classes a serem instanciadas no código, e, módulos úteis
from livro import Livro
from usuario import Usuario
import os

# Variável global
livros = [] # Lista de livros cadastrados
usuarios = [] # Lista de usuários cadastrados
emprestimos = [] # Lista de emprestimos realizados

def menuPrincipal():
    print('*************  MENU  *************')
    print('[1] Cadastrar um novo Livro')
    print('[2] Cadastrar um novo Usuário')
    print('[3] Realizar um empréstimo')
    print('[4] Realizar uma devolução')
    print('[5] Consulta de Livros')
    print('[6] Consulta de Usuários')
    print('[7] Relatórios')
    print('[0] Encerrar o programa')
    print('**********************************')
    
    opc = None
    
    while (opc != '0'):
        opc = input('MENU OPÇÃO: ')

        if opc == '1':
            return cadastrarLivro()
        elif opc == '2':
            return cadastrarUsuário()
        elif opc == '3':
            return fazerEmprestimo()
        elif opc == '4':
            return fazerDevolucao()
        elif opc == '5':
            return consultarLivros()
        elif opc == '6':
            return consultarUsuarios()
        elif opc == '7':
            return obterRelatorios()
        
    os.system('clear')
    print('*********************  FIM  ********************')
    print('OBRIGADO POR USAR NOSSO SISTEMA DE GERENCIAMENTO')
    
def cadastrarLivro():
    os.system('clear')
    print("*****  CADASTRO DE LIVROS  *****")

    # Recebe os valores do título, autor e ano de publicação do livro
    titulo = input('Título do Livro: ')
    autor = input('Autor do Livro: ')
    ano = input('Ano de Publicação: ')     
    
    # Tratativa para validar o valor da variável 'copias', pois, irei operar matematicamente com ela em outros métodos
    copias = None
    while True:
        try:
            # Solicita o input e tenta converter para inteiro
            copias = int(input('Número de Cópias: '))
            
            # Verifica se o valor é positivo
            if copias < 0:
                print("Insira um Número de Cópias inteiro!")
            else:
                # Se for um valor válido, sai do loop
                break
        except ValueError:
            # Trata o caso de o input não ser um número inteiro
            print("Entrada inválida! Por favor, insira um número inteiro válido.")
    
    # Cria uma instância do objeto Livro
    livro = Livro(titulo, autor, ano, copias)
    # Adiciona o novo livro a uma lista de livros
    livros.append(livro)
    
    print("-----------------------------------------------------------------------")
    input("LIVRO cadastrado com Sucesso! (Pressione 'Enter' para retornar ao Menu Principal)")
    os.system('clear')
    menuPrincipal()
    
def cadastrarUsuário():
    os.system('clear')
    print("*****  CADASTRO DE USUÁRIOS  *****")
    
    # Recebe os valores do nome e contato do usuário
    nome = input('Nome do usuário: ')
    contato = input('Telefone para contato: ') # OBS: O código está simplificado e não verifica se é um Telefone válido
    
    # Tratativa para validar o input da variável 'identificacao'
    id = None
    while True:
        # Recebe o valor do identificador, usando CPF como exemplo.
        id = input('Número de identificação (CPF): ') # OBS: O código está simplificado e não verifica se é um CPF válido
        
        id_unico = False
        for usuario in usuarios:
            # Verifica se existe algum usuário com o mesmo número de identificação digitado
            if usuario.identificacao == id:
                print(f'Já existe um(a) usuário(a) ({usuario.nome}) com esta mesma identificação (CPF)!')
                print('Tentar novamente? Sim [Enter] | Não [n]')
                resposta = input()
                if resposta == 'n' or resposta == 'N':
                    os.system('clear')
                    menuPrincipal()
                id_unico = True
                break
        if not id_unico:
            # Se nenhum usuário foi encontrado, o loop termina e o número de identificação é considerado único
            break 
    
    # Cria uma instância do objeto Usuario
    usuario = Usuario(nome, id, contato)
    # Adiciona o novo usuário a uma lista de usuários
    usuarios.append(usuario)
    
    print("-----------------------------------------------------------------------")
    input("USUÁRIO cadastrado com Sucesso! (Pressione 'Enter' para retornar ao Menu Principal)")
    os.system('clear')
    menuPrincipal()
 
def fazerEmprestimo():
    os.system('clear')
    print("*****  EMPRESTIMO DE LIVROS  *****")
    usuario_selecionado = None
    livro_selecionado = None
    
    print("\n** ESCOLHA O USUÁRIO RESPONSÁVEL PELO EMPRÉSTIMO **")
    usuarios_encontrados = _buscaUsuario() # Realiza uma busca na lista completa de usuário
    if usuarios_encontrados:
        for indice, usuario in enumerate(usuarios_encontrados):
            # Percorre todos os itens da lista filtrada de usuários e exibe o valor dos atributos de forma personalizada
            print(f'[{indice +1}] {usuario.nome} | CPF:{usuario.identificacao}')

        try:
            usuarioIndice = int(input("\nDigite o NÚMERO correspondente ao USUÁRIO que fará o empréstimo: "))
            usuarioIndice = usuarioIndice -1 # Necessário fazer esse ajuste pois os indices de uma lista sempre iniciam em 0
            # Verifica se o índice está dentro do intervalo válido
            if (0 <= usuarioIndice < len(usuarios_encontrados)):
                usuario_selecionado = usuarios_encontrados[usuarioIndice]
            else:
                input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                os.system('clear')
                menuPrincipal()
        except ValueError:
            input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
            os.system('clear')
            menuPrincipal()

        print("\n** ESCOLHA O LIVRO A SER EMPRESTADO **")
        livros_encontrados = _buscaLivro() # Realiza uma busca na lista completa de livros
        if livros_encontrados:
            for indice, livro in enumerate(livros_encontrados):
                # Percorre todos os itens da lista filtrada de livros e exibe o valor dos atributos de forma personalizada
                print(f'[{indice +1}] {livro.titulo} - {livro.autor} - {livro.ano} | {livro.copias} cópias disponíveis')
            
            try:
                livroIndice = int(input("Digite o NÚMERO correspondente ao LIVRO que será emprestado: "))
                livroIndice = livroIndice -1 # Necessário fazer esse ajuste pois os indices de uma lista sempre iniciam em 0
                # Verifica se o índice está dentro do intervalo válido
                if (0 <= livroIndice < len(livros_encontrados)):
                    livro_selecionado = livros_encontrados[livroIndice]
                    
                    # Verificar a disponibilidade do livro antes de confirmar o empréstimo.
                    if livro_selecionado.copias == 0:
                        input("O LIVRO escolhido NÃO POSSUE uma cópia disponível no momento\n(Pressione 'Enter' para retornar ao Menu Principal)")
                        os.system('clear')
                        menuPrincipal()
                        
                    # Encontra dentro da lista de livros a instância do livro selecionado no emprestimo
                    for livro in livros:
                        if livro == livro_selecionado:
                            livro.copias -= 1  # Atualizar o número de cópias disponíveis após o empréstimo
                            print(f"\nEmpréstimo realizado com sucesso para {usuario_selecionado.nome}!")
                            print(f"Número de Cópias atualizadas: {livro.copias}un disponíveis para o livro '{livro.titulo}'")
                            
                            emprestimos.append({'usuario': usuario_selecionado, 'livro': livro}) # Atualiza a lista de empréstismos com o Usuário e Livro selecionado
                            break
                        
                    print("---------------------------------------------------")
                    input("Pressione 'Enter' para retornar ao Menu Principal")
                    os.system('clear')
                    menuPrincipal()
                else:
                    input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                    os.system('clear')
                    menuPrincipal()
                    
            except ValueError:
                input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                os.system('clear')
                menuPrincipal()

def fazerDevolucao():
    os.system('clear')
    print("*****  DEVOLUÇÃO DE LIVROS  *****")

def consultarLivros():
    os.system('clear')
    print("*****  CONSULTA DE LIVROS  *****")
    
    livros_encontrados = _buscaLivro() # Realiza uma busca na lista completa de livros
    
    if livros_encontrados:
        for indice, livro in enumerate(livros_encontrados):
            # Percorre todos os itens da lista filtrada de livros e exibe o valor dos atributos de forma personalizada
            print(f'{indice +1}.: {livro.titulo} - {livro.autor} - {livro.ano} | {livro.copias} cópias disponíveis')
    else:
        print('Nenhum livro encontrado')
        
    print("---------------------------------------------------")
    input("Pressione 'Enter' para retornar ao Menu Principal")
    os.system('clear')
    menuPrincipal()
 
def consultarUsuarios():
    os.system('clear')
    print("*****  CONSULTA DE USUÁRIOS  *****")
    
    usuarios_encontrados = _buscaUsuario() # Realiza uma busca na lista completa de usuário
            
    if usuarios_encontrados:
        for indice, usuario in enumerate(usuarios_encontrados):
            # Percorre todos os itens da lista filtrada de usuários e exibe o valor dos atributos de forma personalizada
            print(f'{indice +1}.: {usuario.nome} - {usuario.contato} - {usuario.identificacao}')
    else:
        print('Nenhum usuário encontrado')
        
    print("---------------------------------------------------")
    input("Pressione 'Enter' para retornar ao Menu Principal")
    os.system('clear')
    menuPrincipal()

# Método auxiliar que retorna a lista filtrada de livros. Criada para reutilização de código
def _buscaLivro():
    print("Digite uma palavra referente ao TÍTULO, AUTOR ou ANO DE PUBLICAÇÃO (Pressione [Enter] para ver a lista completa): ")
    busca = input()
    busca = busca.lower() # Converte o tempo da busca em minuscula para garantir a igualdade da comparação com o valor dos atributos 
    
    livros_encontrados = [] # Variável para armazenar os livros que correspondem a busca
    for livro in livros:
        if ((busca in livro.titulo.lower()) or (busca in livro.autor.lower()) or (busca in livro.ano.lower())):
            # Adiciona o livro encontrado a lista filtrada de livros
            livros_encontrados.append(livro)
    
    return livros_encontrados

def _buscaUsuario():
    print("Digite uma palavra referente ao: NOME, CONTATO ou NÚMERO INDETIFICADOR (Pressione [Enter] para ver a lista completa):")
    busca = input()
    busca = busca.lower() # Converte o tempo da busca em minuscula para garantir a igualdade da comparação com o valor dos atributos 
    
    usuarios_encontrados = [] # Variável para armazenar os usuários que correspondem a busca
    for usuario in usuarios:
        if ((busca in usuario.nome.lower()) or (busca in usuario.identificacao.lower()) or (busca in usuario.contato.lower())):
            # Adiciona o usuário encontrado a lista filtrada de usuários
            usuarios_encontrados.append(usuario)
            
    return usuarios_encontrados

def obterRelatorios():
    os.system('clear')
    print("*****  RELATÓRIOS  *****")

# Popula as variáveis livros e usuários para facilitar o uso inicial do programa
livros = [
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", '1954', 0),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", '1997', 6),
    Livro("Harry Potter e a Phoenix", "J.K. Rowling", '1997', 3),
    Livro("O Código Da Vinci", "Dan Brown", '2003', 7),
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", '1954', 5),
    Livro("1984", "George Orwell", '1949', 2),
    Livro("Dom Quixote", "Miguel de Cervantes", '1605', 3)
]
usuarios = [
    Usuario('João Silva', '11110', '1'),
    Usuario('João Pedro', '11111', '123456'),
    Usuario('Maria Silva', '11112', '654321'),
    Usuario('Aline Santos', '11113', '112233'),
    Usuario('Joaldo Teixeira', '11114', '332211'),
]

menuPrincipal()