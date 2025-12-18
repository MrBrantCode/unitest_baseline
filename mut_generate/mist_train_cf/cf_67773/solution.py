"""
QUESTION:
Implement a Python function called `aspect_oriented_logging` that demonstrates the principles of Aspect-Oriented Programming (AOP) by separating the cross-cutting concern of logging from the main program logic. The function should take another function as an argument and log its execution, including the arguments passed and the return value. The logging aspect should be modularized and decoupled from the main program logic.
"""

def aspect_oriented_logging(func):
    """
    This is a decorator function that demonstrates Aspect-Oriented Programming (AOP) principles by 
    separating the cross-cutting concern of logging from the main program logic.

    Args:
        func (function): The function to be logged.

    Returns:
        function: A wrapper function that logs the execution of the input function.
    """

    # Define a wrapper function to encapsulate the logging logic
    def wrapper(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with arguments: args={args}, kwargs={kwargs}")
        
        # Execute the input function and store the return value
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"{func.__name__} returned: {result}")
        
        # Return the result of the input function
        return result
    
    # Return the wrapper function
    return wrapper