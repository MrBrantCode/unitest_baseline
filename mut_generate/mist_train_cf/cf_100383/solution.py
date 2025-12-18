"""
QUESTION:
Create a function `create_custom_logger` that takes a log file name and a logging level as input and returns a custom logger object. The logger should have a specific format and should handle exceptions and edge cases effectively. The logging level should be set based on the input, and the logger should be configured to log messages to both the console and a file.
"""

import logging

def create_custom_logger(log_file_name, logging_level):
    """
    Create a custom logger object with a specific format and logging level.
    
    Args:
    log_file_name (str): The name of the log file.
    logging_level (str): The logging level, e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
    
    Returns:
    logger (Logger): A custom logger object.
    """

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, logging_level.upper()))

    # Define the logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(getattr(logging, logging_level.upper()))
    file_handler.setFormatter(formatter)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, logging_level.upper()))
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger