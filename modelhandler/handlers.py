import datetime
import logging

from django.utils.module_loading import import_string

__all__ = ['LogModel']


class LogModel(logging.Handler):
    def __init__(self, model=None, *args, **kwargs):
        self.model = model
        super(LogModel, self).__init__(*args, **kwargs)

    def get_model(self):
        if self.model and isinstance(self.model, str):
            self.model = import_string(self.model)
        if not self.model:
            from modelhandler.models import Log
            self.model = Log
        return self.model

    def emit(self, record):
        """
        :param logging.LogRecord record:
        """
        instance = self.get_model()()
        instance.name = record.name[:255]
        instance.level = record.levelno
        instance.message = record.getMessage()
        instance.created = datetime.datetime.fromtimestamp(record.created)
        instance.filename = record.filename[:255] if isinstance(record.filename, str) else None
        instance.funcName = record.funcName[:255] if isinstance(record.funcName, str) else None
        instance.formatted = self.format(record)
        if record.exc_info:
            formatter = self.formatter or logging.Formatter()
            instance.traceback = formatter.formatException(record.exc_info)
        instance.save()
