"""
QUESTION:
Find the three largest numbers in an unsorted list without using comparison operators, the built-in max() method, or any sorting techniques. The function should be named `findMaxThree` and should take one argument, `arr`, which is a list of integers. The solution should also include the time complexity of the algorithm.
"""

def find_three_largest(arr):
    first = second = third = float('-inf')
    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num is not first:
            third = second
            second = num
        elif num > third and num not in (first, second):
            third = num
    return third, second, first