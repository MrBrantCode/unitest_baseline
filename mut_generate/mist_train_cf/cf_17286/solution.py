"""
QUESTION:
Write a function named `check_increasing_subsequence` that takes a list of numbers as input and returns True if the list contains a strictly increasing subsequence of length 5, and False otherwise. The subsequence must be strictly increasing, meaning all numbers must be different.
"""

def check_increasing_subsequence(numbers):
    if len(numbers) < 5:
        return False

    increasing_count = 1  # keeps track of the count of increasing numbers in the subsequence
    last_number = numbers[0]  # keeps track of the last number in the subsequence

    for i in range(1, len(numbers)):
        if numbers[i] > last_number:
            increasing_count += 1
            last_number = numbers[i]
            if increasing_count == 5:
                return True
        elif numbers[i] < last_number:
            increasing_count = 1
            last_number = numbers[i]

    return False