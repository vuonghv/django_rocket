# Django Rocket :rocket: - Django Structure For Real Project

This is a Django structure project that was collected from my work experience. You can use this repo as a start point for your newly Django project.

## What does it support?

1. All project apps are moved into `apps` folder for good structure
2. Different environments has its own settings that extend from `settings/base.py` file, instead of using default Django `settings.py` file:
    * `settings/dev.py` (For Development env)
    * `settings/prod.py` (For Production)
    * And you can add your own file, e.g `settings/test.py` for your Test env.
3. Customize `User` model, so you can extend the model to meet your function without using [profile model](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#extending-the-existing-user-model) method
4. Integrate and pre-config for [Celery Task Queue](http://www.celeryproject.org) include [Scheduled Tasks](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html). I think your project eventually will need a task queue system.
5. Docker compose config. One command to run them all.

## How to run it?

```bash
$ docker-compose up -d
```

Boom, the server is running on: http://localhost:8000

## How to custom

## TODO

1. Integrate Django Rest Framework and Demo API
2. Integrate [Swagger](https://swagger.io) for API document
3. Integrate Django unit tests

## LICENSE
MIT License

Copyright (c) 2018 Vuong Hoang <vuonghv.cs@gmail.com>