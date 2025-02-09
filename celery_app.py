from celery import Celery

app = Celery(
    'federated_learning',
    broker='pyamqp://user:password@rabbitmq//',
    backend='rpc://',
    include=['tasks']
)

if __name__ == '__main__':
    app.start()
