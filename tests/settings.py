import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(BASE_DIR))
SECRET_KEY = '2a@*ye6$(^h5tqsdz(ga!=_gznq#xpox3c7s&h4hq!3#rbds3@'
DEBUG = True

INSTALLED_APPS = [
    'modelhandler',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'handlers': {
        'log_model': {
            'class': 'modelhandler.handlers.LogModel',
            'level': 'DEBUG'
        }
    },
    'loggers': {
        'root': {
            'handlers': ['log_model'],
            'level': 'DEBUG'
        },
    }
}