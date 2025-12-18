"""
QUESTION:
Implement a function `retorno` that takes a list of functions as input and returns a new function. The returned function should execute each function in the list in reverse order when called, passing the input to the first function and the result of each function to the next one, and returning the output of the last function. The returned function should be able to accept any number of positional and keyword arguments, and pass them to the first function in the list.
"""

def retorno(functions):
    def wrapper(*args, **kwargs):
        result = None
        for func in reversed(functions):
            if result is None:
                result = func(*args, **kwargs)
            else:
                result = func(result)
        return result
    return wrapper