"""
QUESTION:
Create a function `binary_search(secret_number)` that takes a secret number between 1 and 1000 as an argument and returns the number of guesses it takes to find the secret number using a binary search algorithm. The function should keep track of the number of guesses and return -1 if the secret number is not found.
"""

def entance(secret_number):
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

    return -1  # If the secret number is not found, return -1