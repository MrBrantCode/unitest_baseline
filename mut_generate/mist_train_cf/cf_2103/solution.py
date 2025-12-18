"""
QUESTION:
Write a function `sum_of_even_squares(lst)` that takes a list of integers as input and returns the sum of the squares of the even numbers in the list. The function should iterate through the list only once, not use built-in functions or methods for finding even numbers or calculating squares, and not use mathematical operators such as multiplication or exponentiation. The function should handle negative even numbers and have a time complexity of O(n), where n is the length of the input list.
"""

def sum_of_even_squares(lst):
    result = 0
    for num in lst:
        square = 0
        temp = abs(num)
        for _ in range(temp):
            square += temp
        if num % 2 == 0:
            result += square
    return result