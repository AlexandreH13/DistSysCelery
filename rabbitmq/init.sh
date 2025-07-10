#!/bin/bash

echo "Iniciando RabbitMQ..."
rabbitmq-server &

echo "Aguardando RabbitMQ inicializar..."
while ! rabbitmqctl status >/dev/null 2>&1; do
  sleep 2
  echo "Aguardando o RabbitMQ..."
done

echo "RabbitMQ está pronto. Configurando usuários e permissões..."

echo "Criando vhost..."
rabbitmqctl add_vhost $VHOST

echo "Criando usuários..."
rabbitmqctl add_user admin "$QUEUE_PASS"
rabbitmqctl set_user_tags admin administrator

echo "Criando permissões..."
rabbitmqctl set_permissions -p dist_sys admin ".*" ".*" ".*"

echo "Configuração concluída!"

wait