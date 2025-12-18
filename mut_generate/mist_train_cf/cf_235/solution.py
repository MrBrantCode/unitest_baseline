"""
QUESTION:
Create a function `find_second_largest` that takes in a list of integers and returns the second largest number in the list. The function should have a time complexity of O(n), where n is the length of the list. The list can contain duplicate numbers, and it is guaranteed that the list will have at least two distinct elements. If the second largest number is not unique, the function can return any of the occurrences.
"""

def find_second_largest(lst):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest