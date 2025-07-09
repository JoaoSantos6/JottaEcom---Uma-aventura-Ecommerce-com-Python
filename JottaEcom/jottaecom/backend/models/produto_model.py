import sqlalchemy as sa
import sqlalchemy.orm

Base = sqlalchemy.orm.declarative_base()

class BaseProduto(Base):
    __table__ = 'produtos'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    nome = sa.Column(sa.Text, nullable=False)
    valor = sa.Column(sa.Float)
    nota = sa.Column(sa.Float)
    quantidade = sa.Column(sa.Integer)
    descricao = sa.Column(sa.Text)
    avaliacoes = sa.Column(sa.Text)
    imagens = sa.Column(sa.Text)
    
    def __repr__(self):
        return (
            f"<BaseProduto"
            f"id={self.id}, " 
            f"nome={self.nome}, "
            f"valor={self.valor}, "
            f"nota={self.nota}, "
            f"quantidade={self.quantidade}, "
            f"descricao='{self.descricao}', "
            f"avaliacoes='{self.avaliacoes}', "
            f"imagens='{self.imagens}>"
        )
    
    
    