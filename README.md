# Gestão de Tarefas

## Instalação e Configuração

Siga os passos abaixo para configurar e executar este projeto no seu ambiente local:

### Passo 1: Clone o repositório
git clone https://github.com/SEU_USUARIO/tarefas-docker.git cd gestao_tarefas


#### Passo 2: Crie um Ambiente Virtual

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos para criar e ativar um ambiente virtual:

```bash
# Instale o virtualenv, se ainda não estiver instalado
pip install virtualenv

# Crie um ambiente virtual (substitua 'venv' pelo nome que você desejar)
python3 -m venv venv


# Ative o ambiente virtual
source env/bin/activate
```

#### Passo 3: Instale as Dependências Python

Com o ambiente virtual ativado, você pode instalar as dependências Python listadas no arquivo requirements.txt usando o pip:

```bash
pip install -r requirements.txt
```

#### Passo 4: Configure as Variáveis de Ambiente
  
  Crie um arquivo .env na raiz do projeto com base no arquivo .env.example:
  
#### Passo 5: Gere uma Chave Secreta
  Para gerar uma chave secreta, execute o seguinte comando no terminal:
  ```
    python -c 'import secrets; print(secrets.token_hex(24))'
  ```
#### Passo 5:  Copie a chave gerada e coloque no arquivo .env:

 Copie a chave gerada e coloque no arquivo .env:

#### Passo 6:  Construa e Inicie os Contêineres

```bash
docker-compose up -d --build
```


#### Passo 7: Inicializar o Banco de Dados
  Para inicializar o banco de dados, execute as migrações com os seguintes comandos:

```bash
docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "Initial migration."
docker-compose exec web flask db upgrade
```
#### Passo 7: Acesse a Aplicação
  Abra o navegador e acesse
  ```
  http://localhost:5001.
  ```

#### Passo 8: Executar os Testes
  Para rodar os testes unitários, use o seguinte comando:
```
docker-compose run test
```
# gestao-tarefa
# gestao-tarefa
