"""
QUESTION:
Write a function `log_to_stream` that logs a message to a specified stream and returns the logged message. The function should set the logger level to INFO, remove any existing handlers, and log the message at the INFO level. The stream should be an instance of io.StringIO. The function should not log anything to the console.
"""

import logging
import io

def log_to_stream(message):
    """
    Logs a message to a specified stream and returns the logged message.
    
    Args:
    message (str): The message to be logged.
    
    Returns:
    str: The logged message.
    """
    logger = logging.getLogger(__name__)
    stream = io.StringIO()

    logger.setLevel(logging.INFO)  # set logger level
    log_handler = logging.StreamHandler(stream)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_format)
    log_handler.setLevel(logging.INFO)

    # clear any existing handlers
    if (logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(log_handler)
    logger.info(message)
    return stream.getvalue()