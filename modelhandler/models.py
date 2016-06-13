import logging

from django.db import models


class Log(models.Model):
    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField(default=0, choices=logging._levelToName.items())
    message = models.TextField()
    traceback = models.TextField(default=None, null=True, blank=True)
    filename = models.CharField(max_length=255, default=None, null=True, blank=True)
    funcName = models.CharField(max_length=255, default=None, null=True, blank=True)
    created = models.DateTimeField()
    formatted = models.TextField()

    class Meta:
        ordering = ['created']
        get_latest_by = 'created'

    @property
    def levelname(self):
        return logging.getLevelName(self.level)

    def __str__(self):
        return self.message
