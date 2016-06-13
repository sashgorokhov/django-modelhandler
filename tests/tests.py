import logging
import os

from django.test import TestCase
from modelhandler.handlers import LogModel
from modelhandler.models import Log


class TestModelHandler(TestCase):
    def setUp(self):
        self.handler = LogModel(model=Log, level=logging.DEBUG)
        self.logger = self.get_logger(self.__class__.__name__)

    def get_logger(self, name="", level=logging.DEBUG, handler=None):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler or self.handler)
        return logger

    def test_name(self):
        self.logger.info("")
        self.assertTrue(Log.objects.filter(name=self.logger.name).exists())

    def test_root_logger_name(self):
        logger = self.get_logger()
        logger.info("")
        self.assertTrue(Log.objects.filter(name=logger.name).exists())

    def test_levels(self):
        self.logger.debug('Info!')
        for level, levelname in logging._levelToName.items():
            if not self.logger.isEnabledFor(level):
                continue
            self.logger.log(level, "")
            log = Log.objects.latest()
            self.assertEqual(log.level, level)
            self.assertEqual(log.levelname, levelname)

    def test_traceback(self):
        message = 'My Message'
        try:
            raise ValueError(message)
        except:
            self.logger.exception("")
        log = Log.objects.latest()
        self.assertTrue(log.traceback)
        self.assertIn(message, log.traceback)

    def test_filename(self):
        self.logger.debug("")
        self.assertTrue(Log.objects.filter(filename=os.path.split(__file__)[-1]).exists())

    def test_funcname(self):
        self.logger.debug("")
        self.assertTrue(Log.objects.filter(funcName='test_funcname').exists())

    def test_message(self):
        message = 'Hello, %s'
        param = 'world'
        self.logger.debug(message, param)
        log = Log.objects.latest()
        self.assertEquals(log.message, message % param)