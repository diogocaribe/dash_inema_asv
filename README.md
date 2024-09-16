# Construindo um ambiente local

## Este procedimento é feito para construir uma virtualenv utilizando o poetry

### O poetry deve estar instalado

Seguir os comandos abaixo

```bash
# Entrar na pasta do projeto
cd dash_inema_asv
# Exetutar o comando 
poetry install
# Para ativar o ambiente virtual
poetry shell

cd dash_inema_asv
```
```python
# Executando a aplicação em modo debug
python -m dash_inema_asv.index
```
A execução foi realizada como um modulo por que de outra maneira estava dando erro na importação de modulos dentro da aplicação quando executada com o servidor web (guvicorn - wsgi).
##
# Para rodar a aplicação com o Docker (ambiente de produção)


```dash
docker compose up -d --remove-orphans

docker-compose down --remove-orphans
```
##
# Perguntas para responder

1. Quantidade de asv concedida calculado pelo polígono gravado no SEIA no tempo?

2. Qual a diferença entre a área concedida e a área calcula a partir dos poligonos gravados no SEIA no tempo?

    Esta pergunta foi respondida para termos um indicador de como esta a diferença entre a área concedida no sistema e a área calculada a partir da geometria fornecida.