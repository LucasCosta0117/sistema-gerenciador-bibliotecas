
class Usuario:
    # Método construtor e atributos associados à classe
    def __init__(self, nome: str, identificacao: int, contato: int):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato

    # Getter para o nome do usuário
    @property
    def nome(self) -> str:
        return self._nome

    # Setter para o nome do usuário
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self._nome = nome
        else:
            raise ValueError("O nome deve ser um texto (string)!")

    # Getter para o número de identificação
    @property
    def identificacao(self) -> int:
        return self._identificacao

    # Setter para o número de identificação
    @identificacao.setter
    def identificacao(self, id: int):
        if isinstance(id, int) and id > 0:
            self._identificacao = id
        else:
            raise ValueError("A identificacao deve ser um inteiro positivo (int)!")

    # Getter para o contato
    @property
    def contato(self) -> int:
        return self._contato

    # Setter para o contato
    @contato.setter
    def contato(self, contato: int):
        if isinstance(contato, int) and contato > 0:
            self._contato = contato
        else:
            raise ValueError("O contato deve ser um inteiro positivo (int)!")