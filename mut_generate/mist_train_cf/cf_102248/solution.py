"""
QUESTION:
Write a function `get_even_numbers` that takes a list of integers as input. The function should return a new list containing distinct even numbers from the input list, including negative integers with even absolute values, with a time complexity of O(n).
"""

def get_even_numbers(lst):
    even_numbers = []
    seen_numbers = set()

    for num in lst:
        if num % 2 == 0 or abs(num) % 2 == 0:
            if num not in seen_numbers:
                even_numbers.append(num)
                seen_numbers.add(num)

    return even_numbers