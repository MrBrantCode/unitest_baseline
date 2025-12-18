"""
QUESTION:
Create a function `calculate_inverse_sum(n)` that calculates the sum of the inverses of numbers from 1 to `n` (inclusive) while implementing a logging system to record each exception and its accompanying 'i' value. The function should terminate and return the sum of the non-error inverses if more than 3 exceptions occur. Use a logging system to log exceptions to a file named `exception.log`.
"""

import logging

def calculate_inverse_sum(n):
    logging.basicConfig(filename='exception.log', level=logging.ERROR)
    sum_inverse = 0.0
    exception_count = 0

    for i in range(1, n+1):
        try:
            sum_inverse += 1/i
        except Exception as e:
            exception_count += 1
            logging.error(f"An exception ({e}) occurred at 'i' = {i}")
            
            if exception_count > 3:
                break

    return sum_inverse