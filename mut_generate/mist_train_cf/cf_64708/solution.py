"""
QUESTION:
Create a function `hello` that takes one argument `name` of any data type. The function should return a personalized greeting if `name` is a non-empty string. If `name` is an empty string, it should return 'Hello!'. If `name` is not a string, the function should return an error message. The function should also handle potential exceptions and return the error message.
"""

def hello(name=''):
    try:
        # Check if the variable 'name' is of type string
        if type(name) is not str:
            return 'The variable `name` should be a string.'

        # Check if 'name' is an empty string
        elif name.strip() == '':
            return 'Hello!'

        # If 'name' is not an empty string
        else:
            return 'Hello, ' + name.strip() + '!'
    except Exception as e:
        return str(e)