"""
QUESTION:
Create a Python decorator `with_config_key` that accepts a configuration key and a custom exception as arguments. The decorator should validate the presence of the specified configuration key in the task class's configuration dictionary and raise the custom exception if the key is missing. The custom exception `WriterTaskConfigInvalid` should be defined and used by the `with_config_key` decorator. The decorator should be reusable to validate multiple configuration keys.
"""

class WriterTaskConfigInvalid(Exception):
    pass

def with_config_key(key, raise_exc):
    def decorator(cls):
        def wrapper(*args, **kwargs):
            if key not in kwargs.get('config', {}):
                raise raise_exc
            return cls(*args, **kwargs)
        return wrapper
    return decorator