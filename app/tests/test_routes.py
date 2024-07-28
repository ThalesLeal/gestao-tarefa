import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app, db
from app.models import Tarefa
from config import TestConfig

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Gestão de Tarefas', response.get_data(as_text=True))

    def test_add_tarefa(self):
        response = self.client.post('/add', data=dict(titulo='Teste', descricao='Teste descricao'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Teste', response.get_data(as_text=True))

    def test_update_tarefa(self):
        tarefa = Tarefa(titulo='Teste', descricao='Teste descricao')
        db.session.add(tarefa)
        db.session.commit()

        response = self.client.post(f'/update/{tarefa.id}', data=dict(concluida=True), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Desmarcar Conclusão', response.get_data(as_text=True))

    def test_delete_tarefa(self):
        tarefa = Tarefa(titulo='Teste', descricao='Teste descricao')
        db.session.add(tarefa)
        db.session.commit()

        response = self.client.get(f'/delete/{tarefa.id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Teste', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
