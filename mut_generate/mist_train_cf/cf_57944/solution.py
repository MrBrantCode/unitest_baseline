"""
QUESTION:
Create a Python function named `aspect_oriented_example` that demonstrates the principles of Aspect-Oriented Programming (AOP). The function should log all function calls with names that begin with 'set' without modifying the original code.
"""

def aspect_oriented_example(original_function):
    """
    A function that demonstrates the principles of Aspect-Oriented Programming (AOP).
    It logs all function calls with names that begin with 'set' without modifying the original code.
    """
    
    # Check if the original function's name begins with 'set'
    if original_function.__name__.startswith('set'):
        
        # Define a new function that will wrap the original function
        def wrapper(*args, **kwargs):
            # Log the function call
            print(f"Calling function: {original_function.__name__}")
            
            # Call the original function
            return original_function(*args, **kwargs)
        
        # Return the wrapper function
        return wrapper
    
    # If the original function's name does not begin with 'set', return the original function
    else:
        return original_function