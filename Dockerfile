# syntax=docker/dockerfile:1

FROM python:3.11.2-slim as base

# Não gera arquivos pyc.
ENV PYTHONDONTWRITEBYTECODE=1

# Sempre exibe stdin e stdput.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Atribui volumes de cache para build mais rápido.
# Instala dependências Python.
# Instala Curl (para healthcheck).
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
