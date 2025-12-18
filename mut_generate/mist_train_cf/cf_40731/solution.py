"""
QUESTION:
Create a function `create_log_manager` that takes in three parameters: `name` (a string representing the name for the log manager), `filepath` (a string representing the file path for the log file), and `level` (a string representing the log level, which can be CRITICAL, ERROR, WARNING, INFO, or DEBUG). The function should return a configured log manager that can be used to log messages to the specified file with the given log level. The log manager should be created using the Python `logging` module.
"""

import logging

def create_log_manager(name, filepath, level):
    logger = logging.getLogger(name)
    log_level = getattr(logging, level.upper())
    logger.setLevel(log_level)
    
    file_handler = logging.FileHandler(filepath)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger