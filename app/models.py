from app import db
from datetime import datetime
import pytz

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.String(256))
    concluida = db.Column(db.Boolean, default=False)
    data_criacao = db.Column(db.DateTime, default=lambda: datetime.now(pytz.timezone('America/Sao_Paulo')))
    data_conclusao = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Tarefa {self.titulo}>'
