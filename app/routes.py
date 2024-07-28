from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Tarefa
from app import db
from datetime import datetime
import pytz

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    tarefas = Tarefa.query.all()
    for tarefa in tarefas:
        tarefa.data_criacao = tarefa.data_criacao.astimezone(pytz.timezone('America/Sao_Paulo'))
        if tarefa.data_conclusao:
            tarefa.data_conclusao = tarefa.data_conclusao.astimezone(pytz.timezone('America/Sao_Paulo'))
    return render_template('index.html', tarefas=tarefas)

@bp.route('/add', methods=['POST'])
def add():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    tarefa = Tarefa(titulo=titulo, descricao=descricao, data_criacao=datetime.now(pytz.timezone('UTC')))
    db.session.add(tarefa)
    db.session.commit()
    return redirect(url_for('.index'))

@bp.route('/update/<int:tarefa_id>', methods=['POST'])
def update(tarefa_id):
    tarefa = db.session.get(Tarefa, tarefa_id)
    if tarefa:
        tarefa.concluida = not tarefa.concluida
        if tarefa.concluida:
            tarefa.data_conclusao = datetime.now(pytz.timezone('UTC'))
        else:
            tarefa.data_conclusao = None
        db.session.commit()
    return redirect(url_for('.index'))

@bp.route('/edit/<int:tarefa_id>', methods=['GET'])
def edit(tarefa_id):
    tarefa = db.session.get(Tarefa, tarefa_id)
    if tarefa:
        return render_template('edit.html', tarefa=tarefa)
    return redirect(url_for('.index'))

@bp.route('/edit/<int:tarefa_id>', methods=['POST'])
def update_task(tarefa_id):
    tarefa = db.session.get(Tarefa, tarefa_id)
    if tarefa:
        tarefa.titulo = request.form['titulo']
        tarefa.descricao = request.form['descricao']
        db.session.commit()
    return redirect(url_for('.index'))

@bp.route('/delete/<int:tarefa_id>')
def delete(tarefa_id):
    tarefa = db.session.get(Tarefa, tarefa_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect(url_for('.index'))
