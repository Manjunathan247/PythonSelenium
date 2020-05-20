import inspect
import logging
import pytest


def getLogger(logLevel=logging.INFO):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler(loggerName+".log".format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger


@pytest.mark.usefixtures("driver_init")
class Base_Test:
    pass
