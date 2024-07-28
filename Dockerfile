# Use a imagem base do Python
FROM python:3.10-slim

# Instala as dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libsasl2-dev \
    python3-dev \
    libldap2-dev \
    libssl-dev \
    libsasl2-modules-gssapi-mit

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt requirements.txt
RUN pip install pytest

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto para o diretório de trabalho
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=run.py

# Expõe a porta 5000 para o Flask
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
