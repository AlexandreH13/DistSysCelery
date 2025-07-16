'''
Api to simulate a producer that sends messages to RabbitMQ.
'''

from celery import Celery

from config.logger import logger
from config.properties import RABBITMQ_USER, RABBITMQ_PASS, RABBITMQ_HOST, RABBITMQ_PORT, VHOST

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Producer API",
)

celery_app = Celery("send_task", broker=f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{VHOST}")

celery_app.conf.timezone = "America/Sao_Paulo"
celery_app.conf.update(task_track_started=True, worker_send_task_events=True)

class ProducerMessage(BaseModel):
    id_message: str
    message: str
    size: int

@app.post("/producer_consumer")
def send_message(message: ProducerMessage):
    """
    Simulates sending a message to RabbitMQ.
    In a real application, this function would use a RabbitMQ client to send the message.
    """

    id_message = message.id_message
    message_content = message.message
    size = message.size

    producer_consumer_celery(message_content, size)
    return JSONResponse(
        content={"detail": f"Message with ID {id_message} sent successfully."},
        status_code=200,
)

def producer_consumer_celery(message: str, size: int) -> None:
    """
    A basic producer consumer function
    """
    logger.info(f"Sending message: {message} with size: {size}")
    task = celery_app.send_task(
        "producer_consumer",
        args=[message, size],
        queue="producer_consumer_queue",
    )
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


