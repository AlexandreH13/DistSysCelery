#!/bin/bash

# Função para verificar se um comando foi bem-sucedido
check_service_status() {
  if [ $? -ne 0 ]; then
    echo "Erro ao iniciar $1. Abortando."
    exit 1
  fi
}

# Inicia o Celery Worker
echo "Iniciando Celery Worker..."
celery -A consumer worker --loglevel=info
check_service_status "Celery Worker"
echo "Celery Worker iniciado com sucesso."