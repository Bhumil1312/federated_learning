FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install celery
CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info"]
