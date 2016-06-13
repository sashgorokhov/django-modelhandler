python-telegram-handler
***********************

.. image:: https://badge.fury.io/py/django-modelhandler.svg
    :target: https://badge.fury.io/py/django-modelhandler

.. image:: https://travis-ci.org/sashgorokhov/django-modelhandler.svg?branch=master
    :target: https://travis-ci.org/sashgorokhov/django-modelhandler

A python logging handler that saves logs into django model. That's it.

Installation
============

Via pip:

.. code-block:: shell

    pip install django-modelhandler

Usage
=====

Add ``modelhandler`` to your INSTALLED_APPS, then, configure log handler in your desired way.
For example, using dictConfig:

.. code-block:: python

    {
        'version': 1,
        'handlers': {
            'modelhandler': {
                'class': 'modelhandler.handlers.LogModel',
                'level': 'ERROR'
            }
        },
        'loggers': {
            'my_logger': {
                'handlers': ['modelhandler'],
                'level': 'ERROR'
            }
        }
    }

Run migrations that will create a ``Log`` model:

.. code-block:: shell

    python manage.py migrate

And now you can start logging in django model.

Getting logs:

.. code-block:: python

    from modelhandler.models import Log
    # Get the latest log
    log = Log.objects.latest()
    log.name # logger name
    log.level # logging level integer
    log.levelname # logging level as string (DEBUG, INFO, etc.)
    log.message # the log message
    log.traceback # traceback, if exists. default: None
    log.filename # filename (with ext) where the log was sent
    log.funcName # function name where the log was sent
    log.created # log creation datetime
    log.formatted # the log message as if it was written in file. (with [datetime] [level] etc.)


If you have a django admin enabled, then you can browse your logs on model Log of application modelhandler.
It has a customized modeladmin to enabale filtering by logger name and levelname, and searching by message.

If you would like to customize a log model (to alter models Meta), then just subclass a ``modelhandler.models.Log``
model, do whatever you want and add your model to LogModel handler parameters:

.. code-block:: python

    'handlers': {
        'modelhandler': {
            'class': 'modelhandler.handlers.LogModel',
            'model': 'path.to.your.model'
            'level': 'ERROR'
        }
    }

If you using celery in your project then you might want to add some model cleaning tasks in ``CELERYBEAT_SCHEDULE``:

.. code-block:: python

    CELERYBEAT_SCHEDULE = {
        'cleanup_day': {
            'task': 'modelhandler.tasks.cleanup_day',
            'schedule': timedelta(days=1)
        }, # OR
        'cleanup_week': {
            'task': 'modelhandler.tasks.cleanup_week',
            'schedule': timedelta(days=7)
        }, # OR
        'cleanup_month': {
            'task': 'modelhandler.tasks.cleanup_month',
            'schedule': timedelta(days=30)
        }
    }

``modelhandler.tasks.cleanup_day`` will delete all logs that are older than one day from time of task execution.
``modelhandler.tasks.cleanup_week`` and ``modelhandler.tasks.cleanup_month`` are similar.

If you want to customize the time of deletion, there is a task ``modelhandler.tasks.cleanup_logs`` that accepts
a ``before`` parameter that must be a datetime object or None (in this case a value of timezone.now() will be taken).
There is no magic: just ``Log.objects.filter(created__lte=before).delete()``
