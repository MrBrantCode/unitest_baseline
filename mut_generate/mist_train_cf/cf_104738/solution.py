"""
QUESTION:
Create a function `traverse_and_print` that takes a list of integers as input and prints each element in sequence, skipping numbers divisible by 3. The function should also keep track of and return the count of numbers skipped.
"""

def traverse_and_print(numbers):
    count_skipped = 0
    for num in numbers:
        if num % 3 == 0:
            count_skipped += 1
        else:
            print(num)
    return count_skipped