class Livro:
    def __init__(self, titulo: str, autor: str, ano: str, copias: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias = copias

    # Getter para o título
    @property
    def titulo(self) -> str:
        return self._titulo

    # Setter para o título
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self._titulo = titulo
        else:
            raise ValueError("O título deve ser um texto (string)!")

    # Getter para o autor
    @property
    def autor(self) -> str:
        return self._autor

    # Setter para o autor
    @autor.setter
    def autor(self, autor: str):
        if isinstance(autor, str):
            self._autor = autor
        else:
            raise ValueError("O autor deve ser um texto (string)!")

    # Getter para o ano de publicação
    @property
    def ano(self) -> str:
        return self._ano

    # Setter para o ano de publicação
    @ano.setter
    def ano(self, ano: str):
        if isinstance(ano, str):
            self._ano = ano
        else:
            raise ValueError("O ano deve ser um texto (string)!")

    # Getter para o número de cópias disponíveis
    @property
    def copias(self) -> int:
        return self._copias

    # Setter para o número de cópias disponíveis
    @copias.setter
    def copias(self, qtd: int):
        if isinstance(qtd, int) and qtd >= 0:
            self._copias = qtd
        else:
            raise ValueError("O número de cópias deve ser um número inteiro!")