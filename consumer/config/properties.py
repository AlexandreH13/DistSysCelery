import os

from dotenv import load_dotenv

load_dotenv()

# CELERY
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
QUEUE_PASS = os.getenv("QUEUE_PASS")
VHOST = os.getenv("VHOST")