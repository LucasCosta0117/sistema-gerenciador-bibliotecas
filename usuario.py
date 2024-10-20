
class Usuario:
    def __init__(self, nome: str, identificacao: str, contato: str):
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
    def identificacao(self) -> str:
        return self._identificacao

    # Setter para o número de identificação
    @identificacao.setter
    def identificacao(self, id: str):
        if isinstance(id, str):
            self._identificacao = id
        else:
            raise ValueError("A identificação deve ser informada como um texto (string)!")

    # Getter para o contato
    @property
    def contato(self) -> str:
        return self._contato

    # Setter para o contato
    @contato.setter
    def contato(self, contato: str):
        if isinstance(contato, str):
            self._contato = contato
        else:
            raise ValueError("O telefone de contato deve ser informado como um texto (string)!")