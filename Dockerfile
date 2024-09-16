# Use uma imagem base com Python 3.12
FROM python:3.12-slim

# Instale dependências do sistema necessárias para o psycopg
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instale o Poetry
RUN pip install poetry

# Copie o restante dos arquivos do projeto para o contêiner
COPY . /dash_inema_asv

# Crie e defina o diretório de trabalho no contêiner
WORKDIR /dash_inema_asv

# Instale as dependências do projeto usando o Poetry
RUN poetry install --no-root

EXPOSE 8050

# Comando para rodar a aplicação usando gunicorn
CMD ["poetry", "run", "gunicorn", "--workers=2", "--threads=4", "-b 0.0.0.0:8050", "-t 6000", "dash_inema_asv.index:server"]
