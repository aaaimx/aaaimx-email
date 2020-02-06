# AAAIMX EMAILS

## RabbitMQ Docker container
    $ docker run -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

open in browser [http://localhost:15672/](http://localhost:15672/)

## Celery service worker
    $ celery worker -A aaaimxemail --loglevel=INFO

In other terminal

## Django Project

```
```