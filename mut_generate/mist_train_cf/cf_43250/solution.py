"""
QUESTION:
Create a function named `configure_logger` that takes in five parameters: `log_level`, `open_console_log`, `open_file_log`, `log_file_path`, and `log_name`. The function should return a configured logger object. 

The parameters should be used as follows:
- `log_level` (int): The logging level to be set for the logger.
- `open_console_log` (bool): A boolean indicating whether to enable logging to the console.
- `open_file_log` (bool): A boolean indicating whether to enable logging to a file.
- `log_file_path` (str or None): The file path for logging if `open_file_log` is True, or None if logging to a file is not enabled.
- `log_name` (str): The name to be given to the logger.

The function should create a logger object with the specified name and log level. It should then configure the logger to log to the console if `open_console_log` is True and/or to the file specified by `log_file_path` if `open_file_log` is True, using the specified log level. The function should return the configured logger object.
"""

import logging

def configure_logger(log_level, open_console_log, open_file_log, log_file_path, log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if open_console_log:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if open_file_log:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger