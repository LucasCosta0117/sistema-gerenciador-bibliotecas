# Importa as classes a serem instanciadas no código, e, módulos úteis
from livro import Livro
from usuario import Usuario
import os

class SistemaBiblioteca:
    # Método construtor e atributos associados à classe
    def __init__(self, livros:list = [], usuarios:list = [], emprestimos:dict = {},):
        self.livros = livros
        self.usuarios =usuarios
        self.emprestimos = emprestimos

    # Getter para 'livros'
    @property
    def livros(self) -> list:
        return self._livros
    
    # Setter para 'livros'
    @livros.setter
    def livros(self, livros):
        if isinstance(livros, list):
            self._livros = livros
        else:
            raise ValueError("O valor de 'livros' deve ser uma lista!")
    
    # Getter para 'usuarios'
    @property
    def usuarios(self) -> list:
        return self._usuarios
    
    # Setter para 'usuarios'
    @usuarios.setter
    def usuarios(self, usuarios):
        if isinstance(usuarios, list):
            self._usuarios = usuarios
        else:
            raise ValueError("O valor de 'usuarios' deve ser uma lista!")
    
    # Getter para 'emprestimos'
    @property
    def emprestimos(self) -> dict:
        return self._emprestimos
    
    # Setter para 'emprestimos'
    @emprestimos.setter
    def emprestimos(self, emprestimos):
        if isinstance(emprestimos, dict):
            self._emprestimos = emprestimos
        else:
            raise ValueError("O valor de 'emprestimos' deve ser um dicionário!")

    # Método que cria o Menu de Console para interação do usuário com o sistema
    def menuPrincipal(self):
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
        
        menuP = None
        
        while (menuP != '0'):
            menuP = input('MENU OPÇÃO: ')

            if menuP == '1':
                return self.cadastrarLivro()
            elif menuP == '2':
                return self.cadastrarUsuário()
            elif menuP == '3':
                return self.fazerEmprestimo()
            elif menuP == '4':
                return self.fazerDevolucao()
            elif menuP == '5':
                return self.consultarLivros()
            elif menuP == '6':
                return self.consultarUsuarios()
            elif menuP == '7':
                return self.obterRelatorios()
            
        os.system('clear')
        print('*********************  FIM  ********************')
        print('OBRIGADO POR USAR NOSSO SISTEMA DE GERENCIAMENTO')
        
    # Método usado para cadastrar um novo livro no sistema
    def cadastrarLivro(self):
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
        self.livros.append(livro)
        
        print("-----------------------------------------------------------------------")
        input("LIVRO cadastrado com Sucesso! (Pressione 'Enter' para retornar ao Menu Principal)")
        os.system('clear')
        self.menuPrincipal()
    
    # Método usado para cadastrar um novo usuário no sistema   
    def cadastrarUsuário(self):
        os.system('clear')
        print("*****  CADASTRO DE USUÁRIOS  *****")
        
        # Recebe os valores do nome e contato do usuário
        nome = input('Nome do usuário: ')
        contato = input('Telefone para contato: ') # OBS: O código está simplificado e não verifica se é um Telefone válido
        
        # Tratativa para validar o input da variável 'identificacao'
        id = None
        while True:
            id = input('Número de identificação: ') # Recebe o valor do identificador.
            
            id_unico = False
            for usuario in self.usuarios:
                # Verifica se existe algum usuário com o mesmo número de identificação digitado
                if usuario.identificacao == id:
                    print(f'Já existe um(a) usuário(a) ({usuario.nome}) com esta mesma identificação!')
                    print('Tentar novamente? Sim [Enter] | Não [n]')
                    resposta = input()
                    if resposta == 'n' or resposta == 'N':
                        os.system('clear')
                        self.menuPrincipal()
                    id_unico = True
                    break
            if not id_unico:
                # Se nenhum usuário foi encontrado, o loop termina e o número de identificação é considerado único
                break 
        
        # Cria uma instância do objeto Usuario
        usuario = Usuario(nome, id, contato)
        # Adiciona o novo usuário a uma lista de usuários
        self.usuarios.append(usuario)
        
        print("-----------------------------------------------------------------------")
        input("USUÁRIO cadastrado com Sucesso! (Pressione 'Enter' para retornar ao Menu Principal)")
        os.system('clear')
        self.menuPrincipal()

    # Método para realizar um empréstimo de um Livro a um Usuário
    def fazerEmprestimo(self):
        os.system('clear')
        print("*****  EMPRESTIMO DE LIVROS  *****")
        usuario_selecionado = None
        livro_selecionado = None
        
        print("\n** ESCOLHA O USUÁRIO RESPONSÁVEL PELO EMPRÉSTIMO **")
        usuarios_encontrados = self._buscaUsuario() # Realiza uma busca na lista completa de usuário
        if usuarios_encontrados:
            for indice, usuario in enumerate(usuarios_encontrados):
                # Percorre todos os itens da lista filtrada de usuários e exibe o valor dos atributos de forma personalizada
                print(f'[{indice +1}] {usuario.nome} | ID:{usuario.identificacao}')

            try:
                usuarioIndice = int(input("\nDigite o NÚMERO correspondente ao USUÁRIO que fará o empréstimo: "))
                usuarioIndice = usuarioIndice -1 # Necessário fazer esse ajuste pois os indices de uma lista sempre iniciam em 0
                # Verifica se o índice está dentro do intervalo válido
                if (0 <= usuarioIndice < len(usuarios_encontrados)):
                    usuario_selecionado = usuarios_encontrados[usuarioIndice]
                else:
                    # Tratativa de erro para caso o usuário escolha um número fora das opções fornecidas
                    input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                    os.system('clear')
                    self.menuPrincipal()
            except ValueError:
                # Tratativa de erro para caso o usuário digite uma opção que não seja um número inteiro
                input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                os.system('clear')
                self.menuPrincipal()

            print("\n** ESCOLHA O LIVRO A SER EMPRESTADO **")
            livros_encontrados = self._buscaLivro() # Realiza uma busca na lista completa de livros
            if livros_encontrados:
                for indice, livro in enumerate(livros_encontrados):
                    # Percorre todos os itens da lista filtrada de livros e exibe o valor dos atributos de forma personalizada
                    print(f'[{indice +1}] {livro.titulo} - {livro.autor} ({livro.ano}) | {livro.copias} cópias disponíveis')
                
                try:
                    livroIndice = int(input("Digite o NÚMERO correspondente ao LIVRO que será EMPRESTADO: "))
                    livroIndice = livroIndice -1 # Necessário fazer esse ajuste pois os indices de uma lista sempre iniciam em 0
                    # Verifica se o índice está dentro do intervalo válido
                    if (0 <= livroIndice < len(livros_encontrados)):
                        livro_selecionado = livros_encontrados[livroIndice]
                        
                        # Verificar a disponibilidade do livro antes de confirmar o empréstimo.
                        if livro_selecionado.copias == 0:
                            input("O LIVRO escolhido NÃO POSSUE uma cópia disponível no momento\n(Pressione 'Enter' para retornar ao Menu Principal)")
                            os.system('clear')
                            self.menuPrincipal()
                            
                        # Encontra na lista geral de livros a instância do livro selecionado no emprestimo
                        for livro in self.livros:
                            if livro == livro_selecionado:
                                livro.copias -= 1  # Atualizar o número de cópias disponíveis após o empréstimo
                                print(f"\nEmpréstimo realizado com sucesso para {usuario_selecionado.nome}!")
                                print(f"Número de Cópias atualizadas: {livro.copias}un disponíveis para o livro '{livro.titulo}'")
                                
                                self.emprestimos.append({'usuario': usuario_selecionado, 'livro': livro}) # Atualiza a lista de empréstismos, adicionando o Usuário e Livro selecionado
                                break
                        
                        # Finaliza o procedimento de empréstimo e redireciona para o Menu Principal   
                        print("---------------------------------------------------")
                        input("Pressione 'Enter' para retornar ao Menu Principal")
                        os.system('clear')
                        self.menuPrincipal()
                    else:
                        # Tratativa de erro para caso o usuário escolha um número fora das opções fornecidas
                        input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                        os.system('clear')
                        self.menuPrincipal()
                        
                except ValueError:
                    # Tratativa de erro para caso o usuário digite uma opção que não seja um número inteiro
                    input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                    os.system('clear')
                    self.menuPrincipal()

    # Método para realizar a devolução de um Livro feita por um Usuário
    def fazerDevolucao(self):
        os.system('clear')
        print("*****  DEVOLUÇÃO DE LIVROS  *****")
        print("\n** ESCOLHA O USUÁRIO RESPONSÁVEL PELA DEVOLUÇÃO **")
        usuarioId = input('Digite o Número de Identificação do Usuário: ')
        
        usuario_selecionado = None
        livro_selecionado = None
        emprestimo_selecionado = None
        livros_emprestados = []  # Lista para armazenar os livros encontrados
        
        # Percorre a lista de empréstimos para buscar pelos empréstimos do usuário digitado
        for emprestimo in self.emprestimos:
            # Verifica se a identificação do usuário no dicionário é igual ao 'usuarioId'
            if emprestimo['usuario'].identificacao == usuarioId:
                # Adiciona o livro correspondente à lista de livros emprestados, salva o usuário e o empréstimo correspondente
                livros_emprestados.append(emprestimo['livro'])
                usuario_selecionado = emprestimo['usuario']
                emprestimo_selecionado = emprestimo
                
        # Informa todos os livros que estãp emprestados para aquele usuário
        if livros_emprestados:
            print(f"Livros emprestados em nome de {usuario_selecionado.nome} (id: {usuarioId}): ")
            for indice, livro in enumerate(livros_emprestados):
                print(f"[{indice +1}] {livro.titulo} - {livro.autor} - {livro.ano}")
                
            livroIndice = int(input("Digite o NÚMERO correspondente ao LIVRO que será DEVOLVIDO: "))
            livroIndice = livroIndice -1 # Necessário fazer esse ajuste pois os indices de uma lista sempre iniciam em 0
            # Verifica se o índice está dentro do intervalo válido
            if (0 <= livroIndice < len(livros_emprestados)):
                livro_selecionado = livros_emprestados[livroIndice]
                    
                # Encontra na lista geral de livros a instância do livro selecionado na devolução
                for livro in self.livros:
                    if livro == livro_selecionado:
                        livro.copias += 1  # Atualizar o número de cópias disponíveis após o empréstimo
                        print(f"\nDevolução realizada com sucesso em nome de {usuario_selecionado.nome}!")
                        print(f"Número de Cópias atualizadas: {livro.copias}un disponíveis para o livro '{livro.titulo}'")
                        
                        self.emprestimos.remove(emprestimo_selecionado) # Atualiza a lista de empréstismos, removendo o empréstimo do Usuário selecionado
                        break
                
                # Finaliza o procedimento de devolução e redireciona para o Menu Principal   
                print("---------------------------------------------------")
                input("Pressione 'Enter' para retornar ao Menu Principal")
                os.system('clear')
                self.menuPrincipal()
            else:
                # Tratativa de erro para caso o usuário escolha um número fora das opções fornecidas
                input("Entrada inválida! (Pressione 'Enter' para retornar ao Menu Principal)")
                os.system('clear')
                self.menuPrincipal()
        else:
            print(f"Nenhum livro encontrado para o usuário com ID {usuarioId}.")
            input("Pressione 'Enter' para retornar ao Menu Principal")
            os.system('clear')
            self.menuPrincipal()

    # Método para consultar um ou todos livros cadastrados no sistema
    def consultarLivros(self):
        os.system('clear')
        print("*****  CONSULTA DE LIVROS  *****")
        
        livros_encontrados = self._buscaLivro() # Realiza uma busca na lista completa de livros
        
        if livros_encontrados:
            for indice, livro in enumerate(livros_encontrados):
                # Percorre todos os itens da lista filtrada de livros e exibe o valor dos atributos de forma personalizada
                print(f'{indice +1}.: {livro.titulo} - {livro.autor} ({livro.ano}) | {livro.copias} cópias disponíveis')
        else:
            print('Nenhum livro encontrado')
            
        print("---------------------------------------------------")
        input("Pressione 'Enter' para retornar ao Menu Principal")
        os.system('clear')
        self.menuPrincipal()

    # Método para consultar um ou todos usuários cadastrados no sistema
    def consultarUsuarios(self):
        os.system('clear')
        print("*****  CONSULTA DE USUÁRIOS  *****")
        
        usuarios_encontrados = self._buscaUsuario() # Realiza uma busca na lista completa de usuário
                
        if usuarios_encontrados:
            for indice, usuario in enumerate(usuarios_encontrados):
                # Percorre todos os itens da lista filtrada de usuários e exibe o valor dos atributos de forma personalizada
                print(f'{indice +1}.: {usuario.nome}  | ID: {usuario.identificacao} | Contato: {usuario.contato}')
        else:
            print('Nenhum usuário encontrado')
            
        print("---------------------------------------------------")
        input("Pressione 'Enter' para retornar ao Menu Principal")
        os.system('clear')
        self.menuPrincipal()
        
    # Método responsável por gerar os relatórios do sistema
    def obterRelatorios(self):
        os.system('clear')
        print("********* GERAR RELATÓRIOS  ********")
        print('[1] Livros Cadastrados')
        print('[2] Livros Disponíveis')
        print('[3] Livros Emprestados')
        print('[4] Usuários Cadastrados')
        print('[5] Usuários com Empréstimos Ativos')
        print('[0] Retornar ao Menu Principal')
        print('************************************')
        menuR = None
        
        while (menuR != '0'):
            menuR = input('OPÇÃO RELATÓRIO: ')

            if menuR == '1':
                return self._livrosCadastrados()
            elif menuR == '2':
                return self._livrosDisponiveis()
            elif menuR == '3':
                return self._livrosEmprestados()
            elif menuR == '4':
                return self._usuariosCadastrados()
            elif menuR == '5':
                return self._usuariosComEmprestimo()
        
        os.system('clear')
        self.menuPrincipal()
        
    # Método auxiliar que retorna a lista filtrada de livros. Criada para garantir a modularização de código
    def _buscaLivro(self):
        busca = input("Pesquise por TÍTULO, AUTOR ou ANO DE PUBLICAÇÃO (Pressione [Enter] para lista completa): ")
        busca = busca.lower() # Converte o tempo da busca em minuscula para garantir a igualdade da comparação com o valor dos atributos 
        
        livros_encontrados = [] # Variável para armazenar os livros que correspondem a busca
        for livro in self.livros:
            if ((busca in livro.titulo.lower()) or (busca in livro.autor.lower()) or (busca in livro.ano.lower())):
                # Adiciona o livro encontrado a lista filtrada de livros
                livros_encontrados.append(livro)
        
        return livros_encontrados

    # Método auxiliar que retorna a lista filtrada de usuários. Criada para garantir a modularização de código
    def _buscaUsuario(self):
        busca = input("Pesquise por NOME ou NÚMERO INDETIFICADOR (Pressione [Enter] para lista completa): ")
        busca = busca.lower() # Converte o tempo da busca em minuscula para garantir a igualdade da comparação com o valor dos atributos 
        
        usuarios_encontrados = [] # Variável para armazenar os usuários que correspondem a busca
        for usuario in self.usuarios:
            if ((busca in usuario.nome.lower()) or (busca in usuario.identificacao.lower())):
                # Adiciona o usuário encontrado a lista filtrada de usuários
                usuarios_encontrados.append(usuario)
                
        return usuarios_encontrados

    # Método auxiliar que retorna apenas os livros totais cadastrados
    def _livrosCadastrados(self):
        os.system('clear')
        print("*** RELATÓRIO: LIVROS CADASTRADOS  ***")
        
        if self.livros:
            # Variável para armazenar soma do total de cópias
            total_copias = 0
            
            # Percorre a lista de livros
            for indice, livro in enumerate(self.livros):
                print(f'{indice + 1}.: {livro.titulo} - {livro.autor} ({livro.ano}) | Número de Cópias: {livro.copias}')
                total_copias += livro.copias # Acumula a quantidade de cópias de cada livro
            
            total_titulos = len(self.livros) # Obtem o total de títulos cadastrados
            print("-------------------------------------------------------")
            print(f"Total de títulos cadastrados: {total_titulos}")
            print(f"Total de unidades disponíveis: {total_copias}")
        else:
            print("Nenhum livro cadastrado no momento!")
        
        input('\nPressione [Enter] para retornar ao Menu de Relatórios')
        self.obterRelatorios()


    # Método auxiliar que retorna apenas os livros disponíveis para empréstimo
    def _livrosDisponiveis(self):
        os.system('clear')
        print("*** RELATÓRIO: LIVROS DISPONÍVEIS  ***")
        
        livros_disponiveis = [] # Variável para armazenar os livros disponíveis para empréstimo
        total_copias_disponiveis = 0 # Variável para armazenar soma do total de cópias disponíveis
        
        # Percorre a lista de livros
        for livro in self.livros:
            if livro.copias > 0:
                livros_disponiveis.append(livro)
                total_copias_disponiveis += livro.copias # Acumula a quantidade de cópias disponíveis

        # Exibe a lista de livros disponíveis para empréstimo
        if livros_disponiveis:
            for indice, livro in enumerate(livros_disponiveis):
                print(f'{indice + 1}.: {livro.titulo} - {livro.autor} ({livro.ano}) | {livro.copias} cópias disponíveis')

            # Exibe o total de títulos e o total de cópias disponíveis
            total_titulos_disponiveis = len(livros_disponiveis)
            print("-------------------------------------------------------")
            print(f"Total de títulos disponíveis para empréstimo: {total_titulos_disponiveis}")
            print(f"Total de cópias disponíveis para empréstimo: {total_copias_disponiveis}")
        
        else:
            print("Nenhum livro disponível para empréstimo no momento!")
            
        input('\nPressione [Enter] para retornar ao Menu de Relatórios')
        self.obterRelatorios()



    # Método auxiliar que retorna apenas os livros disponíveis para empréstimo
    def _livrosEmprestados(self):
        os.system('clear')
        print("*** RELATÓRIO: LIVROS SOB EMPRÉSTIMO  ***")
        # lista para armazenar os livros emprestados
        livros_emprestados = []
        # Variável para armazenar o total de cópias emprestadas
        total_copias_emprestadas = 0
        # Armazena o número de cópias emprestadas por livro
        contador_copias = {}

        # Percorre a lista de empréstimos
        for emprestimo in self.emprestimos:
            livro = emprestimo['livro']  # Acessa o livro no dicionário do empréstimo
            # Cria uma "chave" única com as informações do livro (título, autor, ano), pois o atributo 'copias' pode variar
            chave_livro = (livro.titulo, livro.autor, livro.ano)
            
            # Acumula o número de cópias emprestadas
            total_copias_emprestadas += 1
            
            # Verifica se o livro já foi adicionado ao contador, senão inicializa com 1
            if chave_livro in contador_copias:
                contador_copias[chave_livro] += 1 # Acrescenta 1 un ao contador ao encontrar o livro
            else:
                contador_copias[chave_livro] = 1 # Inicia o contador
                livros_emprestados.append(livro) # Adicoina o livro à lista de livros emprestados

        # Exibe a lista de livros emprestados
        if livros_emprestados:
            for indice, livro in enumerate(livros_emprestados):
                chave_livro = (livro.titulo, livro.autor, livro.ano)
                numero_copias = contador_copias[chave_livro]  # Obtém o número de cópias emprestadas para esse livro
                print(f'{indice +1}.: {livro.titulo} - {livro.autor} ({livro.ano}) | Cópias emprestadas: {numero_copias}')
            
            # Exibe o total de títulos emprestados e cópias emprestadas
            total_titulos_emprestados = len(livros_emprestados)
            print("-------------------------------------------------------")
            print(f"Total de títulos emprestados: {total_titulos_emprestados}")
            print(f"Total de cópias emprestadas: {total_copias_emprestadas}")
        else:
            print("Nenhum livro está emprestado no momento.")
            
        input('\nPressione [Enter] para retornar ao Menu de Relatórios')
        self.obterRelatorios()

    # Método auxiliar que retorna apenas os livros disponíveis para empréstimo
    def _usuariosCadastrados(self):
        os.system('clear')
        print("*** RELATÓRIO: USUÁRIOS CADASTRADOS ***")
        if self.usuarios:
            # Percorre a lista de livros
            for indice, usuario in enumerate(self.usuarios):
                print(f'{indice +1}.: {usuario.nome}  | ID: {usuario.identificacao} | Contato: {usuario.contato}')
            
            total_usuarios = len(self.usuarios) # Obtem o total de usuários cadastrados
            print("-------------------------------------------------------")
            print(f"Total de usuários cadastrados: {total_usuarios}")
        else:
            print("Nenhum usuário cadastrado no momento!")
            
        input('\nPressione [Enter] para retornar ao Menu de Relatórios')
        self.obterRelatorios()

    # Método auxiliar que retorna apenas os livros disponíveis para empréstimo
    def _usuariosComEmprestimo(self):
        os.system('clear')
        print("*** RELATÓRIO: USUÁRIOS COM EMPRÉSTIMO ATIVO ***")
        # lista para armazenar os usuários com empréstimos ativos
        usuarios_com_emprestimos = []
        # Cria um conjunto set() para garantir que não haja duplicatas
        usuarios_unicos = set()

        # Percorre a lista de empréstimos
        for emprestimo in self.emprestimos:
            usuario = emprestimo['usuario']  # Acessa o usuário no dicionário do empréstimo
            # Cria uma "chave" única com as informações do usuário (nome, identificação)
            chave_usuario = (usuario.nome, usuario.identificacao)

            # Se o usuário ainda não estiver no conjunto de usuários únicos, adiciona
            if chave_usuario not in usuarios_unicos:
                usuarios_com_emprestimos.append(usuario)
                usuarios_unicos.add(chave_usuario)

        # Exibe a lista de usuários com empréstimos ativos
        if usuarios_com_emprestimos:
            for indice, usuario in enumerate(usuarios_com_emprestimos):
                print(f'{indice +1}.: {usuario.nome}  | ID: {usuario.identificacao} | Contato: {usuario.contato}')
                
            total_usuarios_com_emprestimos = len(usuarios_com_emprestimos) # Obtem o total de usuários cadastrados
            print("-------------------------------------------------------")
            print(f"Total de usuários com empréstimos ativos: {total_usuarios_com_emprestimos}")
        else:
            print("Nenhum usuário possui empréstimos ativos.")
            
        input('\nPressione [Enter] para retornar ao Menu de Relatórios')
        self.obterRelatorios()