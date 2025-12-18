"""
QUESTION:
Implement the `calculate_even_sum` function, which takes a list of integers as input and returns the sum, count, and average of all even numbers in the list. The function must use a while loop, cannot use built-in functions or methods that directly handle lists or numbers (like `sum()`, `filter()`, or `reduce()`), and must implement the summation logic manually. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1).
"""

def calculate_even_sum(lst):
    count = 0
    even_sum = 0

    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            count += 1
            even_sum += lst[i]
        i += 1

    even_avg = round(even_sum / count, 2) if count != 0 else 0

    return even_sum, count, even_avg