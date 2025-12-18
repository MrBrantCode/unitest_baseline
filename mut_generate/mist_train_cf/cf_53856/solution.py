"""
QUESTION:
Write a function called `second_highest_even_element` that finds the second highest even number in a list of integers. The function should not use built-in functions and should work for both positive and negative numbers. If the list does not contain at least two even numbers, the function should return a message indicating this.
"""

def second_highest_even_element(l: list):
    max1, max2 = float("-inf"), float("-inf")
    for x in l:
        if x % 2 == 0:
            if x > max1:
                max1, max2 = x, max1
            elif x < max1 and x > max2:
                max2 = x
    if max1 == float("-inf") or max2 == float("-inf"):
        return "Not enough even numbers"
    return max2