"""
QUESTION:
Implement a `CustomLogger` class with the following properties and methods:

- The class should have a `level` attribute to determine the minimum severity level of messages to be logged.
- It should have methods to log messages at different severity levels: `debug`, `info`, `warning`, `error`, and `critical`.
- The class should direct the logged messages to appropriate output streams based on their severity level:
  - `debug` and `info` messages should be directed to the console.
  - `warning` messages should be directed to a file named "warning.log".
  - `error` and `critical` messages should be directed to a file named "error.log".
- The `set_level` method should allow changing the logging level dynamically.
"""

import logging

def custom_logger(level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    warning_file_handler = logging.FileHandler('warning.log')
    warning_file_handler.setLevel(logging.WARNING)
    warning_formatter = logging.Formatter('%(levelname)s: %(message)s')
    warning_file_handler.setFormatter(warning_formatter)
    logger.addHandler(warning_file_handler)

    error_file_handler = logging.FileHandler('error.log')
    error_file_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(levelname)s: %(message)s')
    error_file_handler.setFormatter(error_formatter)
    logger.addHandler(error_file_handler)

    class CustomLogger:
        def __init__(self):
            self.level = level

        def set_level(self, level):
            self.level = level

        def debug(self, message):
            if self.level <= logging.DEBUG:
                logger.debug(message)

        def info(self, message):
            if self.level <= logging.INFO:
                logger.info(message)

        def warning(self, message):
            if self.level <= logging.WARNING:
                logger.warning(message)

        def error(self, message):
            if self.level <= logging.ERROR:
                logger.error(message)

        def critical(self, message):
            if self.level <= logging.CRITICAL:
                logger.critical(message)

    return CustomLogger()