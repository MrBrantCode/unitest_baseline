"""
QUESTION:
Write a function named `calculate_even_sum` that takes a list of integers as input and returns the sum of all even numbers in the list, the count of even numbers, and the average of all even numbers rounded to two decimal places. The function must use a while loop and must not use any built-in functions or methods that directly handle lists or numbers, such as `sum()`, `filter()`, or `reduce()`. The solution should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1).
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