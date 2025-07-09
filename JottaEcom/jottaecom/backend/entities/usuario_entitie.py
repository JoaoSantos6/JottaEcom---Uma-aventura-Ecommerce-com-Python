class UsuarioEntities:
    nome: None
    login: None
    senha: None
    email: None
    foto: None
    pedidos: None
    endereco: None
    carrinho: None
    comentarios:None
    
    def __init__(self, nome=None, login=None, senha=None, email=None, foto=None, pedidos=None, endereco=None, carrinho=None, comentarios=None):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.email = email
        self.foto = foto
        self.pedidos = pedidos
        self.endereco = endereco
        self.carrinho = carrinho
        self.comentarios = comentarios

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_foto(self):
        return self.foto

    def set_foto(self, foto):
        self.foto = foto

    def get_pedidos(self):
        return self.pedidos

    def set_pedidos(self, pedidos):
        self.pedidos = pedidos

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_carrinho(self):
        return self.carrinho

    def set_carrinho(self, carrinho):
        self.carrinho = carrinho

    def get_comentarios(self):
        return self.comentarios

    def set_comentarios(self, comentarios):
        self.comentarios = comentarios