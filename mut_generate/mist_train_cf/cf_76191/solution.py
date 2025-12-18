"""
QUESTION:
Create a LogAspect class that adheres to the principles of Aspect-Oriented Programming (AOP) for logging cross-cutting concerns. The class should encapsulate the logging concern without being aware of any business logic. It should also include advices for 'before', 'after', and 'around' a method execution, with meaningful log entries triggered when a method is initiated and completed. The class should use simple and understandable pointcut expressions to match join points, avoiding impacts on unwanted join points.
"""

import functools
import logging

def log_aspect(func):
    """
    A decorator to log method execution.
    
    Args:
        func: The function to be logged.
    
    Returns:
        A wrapper function that logs the execution of the input function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log before the function execution
        logging.info(f"Entering function {func.__name__}")
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Log after the function execution
        logging.info(f"Exiting function {func.__name__}")
        
        return result
    
    return wrapper