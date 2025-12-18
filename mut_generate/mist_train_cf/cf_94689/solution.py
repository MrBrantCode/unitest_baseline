"""
QUESTION:
Write a function `print_combinations` that takes an array of unique integers as input and prints all possible combinations of these integers in a non-repetitive manner. The function should be able to handle arrays of any length, including empty combinations and individual elements.
"""

def print_combinations(arr):
    def generate_combinations(current, remaining, index):
        if index == len(arr):
            print(current)
            return
        generate_combinations(current + [remaining[index]], remaining, index + 1)
        generate_combinations(current, remaining, index + 1)

    generate_combinations([], arr, 0)