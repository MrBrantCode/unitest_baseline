"""
QUESTION:
Write a function `find_second_largest` that takes a list of numbers as input and prints the second largest element. The function should not use any built-in sorting functions and must have a time complexity of O(n) and a space complexity of O(1). The list must have at least two distinct elements.
"""

def find_second_largest(lst):
    if len(lst) < 2:
        print("List must have at least 2 elements")
        return

    largest = float('-inf')
    second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest