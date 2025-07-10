FROM rabbitmq:4.0-management

RUN apt-get update && apt-get install -y curl python3 && rm -rf /var/lib/apt/lists/*

COPY init.sh /init.sh

RUN chmod +x /init.sh

EXPOSE 5672 15672

CMD ["/bin/bash", "/init.sh"]
