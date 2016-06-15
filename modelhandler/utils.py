import logging
from django.utils import six


LEVEL_TO_NAME = dict()
if six.PY3:
    LEVEL_TO_NAME = logging._levelToName
elif six.PY2:
    LEVEL_TO_NAME = {k:v for k, v in logging._levelNames.items() if isinstance(k, int)}