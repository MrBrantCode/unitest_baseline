"""
QUESTION:
Create a function `get_run_generator` that takes a tuple of strings `test_data` as input and returns a callable function. This callable function should generate and return the next input string based on the `test_data` each time it is called. If the `test_data` is exhausted, the function should return an empty string. The generated input strings should be based on the `test_data` and returned in the order they appear in the `test_data`.
"""

from typing import Tuple, Callable, Generator

def get_run_generator(test_data: Tuple[str]) -> Callable[[], str]:
    test_data_gen: Generator[str, None, None] = (line for line in test_data)

    def generate_input() -> str:
        nonlocal test_data_gen
        try:
            return next(test_data_gen)
        except StopIteration:
            return ""

    return generate_input