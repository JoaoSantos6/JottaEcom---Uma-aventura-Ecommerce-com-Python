import sys
import os
import pytest

# Adiciona o backend ao sys.path para importar corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jottaecom/backend')))

from db_connectors.sql_alchemy_manager import SqlAlchemyManager

def test_is_connected():
    manager = SqlAlchemyManager(db_config=None)
    assert manager.is_connected() is True