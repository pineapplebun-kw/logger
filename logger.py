"""
Module for Logging
"""

import logging
import logging.handlers
from pathlib import Path, PurePath

def create_logger(name,
                  loglevel,
                  logfilename,
                  logfile_maxbytes = 1000000,
                  logfile_backupcount=3):
    """ Create System logs """
    Path(PurePath(logfilename).parent).mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" %loglevel)

    #file handler
    filehandler = logging.handlers.RotatingFileHandler(
        filename=logfilename,
        mode="a",
        maxBytes=logfile_maxbytes,
        backupCount=logfile_backupcount,
        encoding=None,
        delay=False
    )
    filehandler.setLevel(logging.DEBUG)

    #console handler
    consolehandler = logging.StreamHandler()
    consolehandler.setFormatter(
        logging.Formatter(
            fmt="{asctime} {name} [{levelname}]: {message}",
            datefmt="%Y-%m-%d %I:%M:%S",
            style="{"
        )
    )
    consolehandler.setLevel(logging.INFO)
    logger.setLevel(numeric_level)
    logger.addHandler(filehandler)
    logger.addHandler(consolehandler)

    return logger