import logging
from datetime import datetime

log_file_location = 'C:/Windows/Temp/'


def get_current_date_time():
    now = datetime.now()
    current_time = now.strftime("%m_%d_%Y_%H_%M_%S")
    return current_time


loggers = {}


def file_logger(name='logName'):
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        _current_time = get_current_date_time()
        handler = logging.FileHandler(f"{log_file_location}" + "Remote_Windows" + f"_{_current_time}" + ".log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        loggers[name] = logger

        return logger
