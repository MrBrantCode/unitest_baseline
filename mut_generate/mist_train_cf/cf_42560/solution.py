"""
QUESTION:
Write a function `longest_consecutive_success(test_results)` that takes in a list `test_results` of integers where positive values represent successful tests and negative values represent failed tests, and returns the length of the longest consecutive sequence of successful tests.
"""

def longest_consecutive_success(test_results):
    max_length = 0
    current_length = 0

    for result in test_results:
        if result > 0:  # Successful test
            current_length += 1
            max_length = max(max_length, current_length)
        else:  # Failed test
            current_length = 0

    return max_length