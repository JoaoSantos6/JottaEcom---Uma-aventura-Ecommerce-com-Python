import sys
import os
import pytest

# Adiciona o backend ao sys.path para importar corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jottaecom/backend')))

from models.produto_model import BaseProduto
from db_connectors.sql_alchemy_manager import SqlAlchemyManager

@pytest.fixture
def manager():
    m = SqlAlchemyManager(db_config=None)
    yield m
    m.dispose_engine()

def test_is_connected(manager):
    assert manager.is_connected() is True
    
def test_context_manager_methods():
    manager = SqlAlchemyManager(db_config=None)
    with manager as db:
        assert db.session is not None
    
def test_busca_linha_unica(manager):
    
    with manager as db:
        
        first_row = db.session.query(BaseProduto).filter_by(id=1).first()
        
        nome_cliente = first_row.nome
        
        assert nome_cliente == 'Camiseta Básica'
        

def test_insere_linha_tabela(manager):

    novo_produto = BaseProduto(
        nome="Produto Teste",
        valor=10.99,
        nota=4.0,
        quantidade=5,
        descricao="Produto inserido pelo teste unitário.",
        avaliacoes='[]',
        imagens='[]'
    )

    print(novo_produto)
    
    with manager as db:
        db.session.add(novo_produto)
        db.session.commit()

        produto_inserido = db.session.query(BaseProduto).filter_by(nome="Produto Teste").first()
        
        # descomentar breakpoint para analisar no banco a insercao
        # Para sair do modo de breakpoint, basta digitar 'q' no terminal
        # breakpoint()
        
        assert produto_inserido is not None
        assert produto_inserido.valor == 10.99

        db.session.delete(produto_inserido)
        db.session.commit()