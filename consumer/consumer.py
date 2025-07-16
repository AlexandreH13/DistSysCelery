from time import sleep
from celery import Celery

from config.properties import RABBITMQ_USER, RABBITMQ_PASS, RABBITMQ_HOST, RABBITMQ_PORT, VHOST

celery_app = Celery("transcritor_tasks", broker=f"pyamqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{VHOST}")

celery_app.conf.task_acks_late = True
celery_app.conf.task_default_queue = f"producer_consumer_queue"
celery_app.conf.timezone = "America/Sao_Paulo"
celery_app.conf.update(task_track_started=True, worker_send_task_events=True)

@celery_app.task(name="producer_consumer")
def consumer_basic(message_content, size):
    print(f"Message received: {message_content} with size: {size}")
    sleep(2)