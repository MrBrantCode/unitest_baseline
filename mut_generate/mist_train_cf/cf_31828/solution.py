"""
QUESTION:
Create a Python decorator function `do_not_track` that takes a single view function as an argument and returns a new function that disables tracking for the original view function. The decorator should work with any view function that takes arbitrary arguments and returns a response.
"""

import typing

def do_not_track(view: typing.Callable) -> typing.Callable:
    """View decorator to disable tracking"""
    def wrapper(*args, **kwargs):
        # Disable tracking logic goes here
        return view(*args, **kwargs)
    return wrapper