"""
QUESTION:
Implement a Python decorator `keyword_checker` that takes a list of keywords as input and checks if any of these keywords are present in the arguments of a function. If a keyword is found, the function should print a warning message and return `None`. If no keywords are present, the function should execute as normal and return its result. The decorator should work with both positional and keyword arguments, and it should convert the arguments to strings before checking for keywords.
"""

def keyword_checker(keywords):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if any(keyword in str(arg) for keyword in keywords):
                    print("Warning: Function contains restricted keyword")
                    return None
            for value in kwargs.values():
                if any(keyword in str(value) for keyword in keywords):
                    print("Warning: Function contains restricted keyword")
                    return None
            return func(*args, **kwargs)
        return wrapper
    return decorator