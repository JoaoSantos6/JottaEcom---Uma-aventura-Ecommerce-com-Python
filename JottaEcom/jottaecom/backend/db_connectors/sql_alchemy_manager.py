import os
import sqlalchemy as sa
import sqlalchemy.orm as orm
import urllib

class SqlAlchemyManager:
    
    def __init__(self, db_config):
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.abspath(os.path.join(base_dir, '..', 'sgbd', 'teste.db'))
        self.engine = sa.create_engine(f"sqlite:///{db_path}")
        print("Engine: ", self.engine)
        
        self.Session = sa.orm.sessionmaker(bind=self.engine, future=True)
        print("Session: ", self.Session)
        
        self.session = None
        
    def __enter__(self):
        self.session = self.Session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
            
    def is_connected(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(sa.text("SELECT 1"))
            return True
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
        
    def dispose_engine(self):
        self.engine.dispose()
        
        
    
        
        