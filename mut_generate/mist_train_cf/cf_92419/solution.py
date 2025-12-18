"""
QUESTION:
Create a function `binary_search(secret_number)` that uses a binary search algorithm to guess a secret number between 1 and 1000, and returns the number of guesses it takes to find the secret number. The function should take an integer `secret_number` as input and return the number of guesses as an integer. The function should not take any other inputs or have any side effects.
"""

def binary_search(secret_number):
    low = 1
    high = 1000
    guesses = 0

    while low <= high:
        mid = (low + high) // 2
        guesses += 1

        if mid == secret_number:
            return guesses
        elif mid < secret_number:
            low = mid + 1
        else:
            high = mid - 1

    return -1