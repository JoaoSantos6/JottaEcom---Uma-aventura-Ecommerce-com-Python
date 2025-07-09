class ProdutoEntities:
    nome: None
    valor: None
    nota: None
    quantidade: None
    descricao: None
    avaliacoes: None
    imagens: None
    
    def __init__(self, nome=None, valor=None, nota=None, quantidade=None, descricao=None, avaliacoes=None, imagens=None):
        self._nome = nome
        self._valor = valor
        self._nota = nota
        self._quantidade = quantidade
        self._descricao = descricao
        self._avaliacoes = avaliacoes
        self._imagens = imagens

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor

    def get_nota(self):
        return self._nota

    def set_nota(self, nota):
        self._nota = nota

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_avaliacoes(self):
        return self._avaliacoes

    def set_avaliacoes(self, avaliacoes):
        self._avaliacoes = avaliacoes

    def get_imagens(self):
        return self._imagens

    def set_imagens(self, imagens):
        self._imagens = imagens