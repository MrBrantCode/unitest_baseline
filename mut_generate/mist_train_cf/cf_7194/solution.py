"""
QUESTION:
Write a function called `find_second_largest` that takes a list of integers as input and returns the second largest integer from the list. The function should not use sorting algorithms or built-in functions. The input list will contain between 2 and 10^5 integers, each ranging from -10^5 to 10^5. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_second_largest(nums):
    largest = float('-inf')  # initialize largest as negative infinity
    second_largest = float('-inf')  # initialize second_largest as negative infinity
    
    for num in nums:
        if num > largest:
            second_largest = largest  # update second_largest as previous largest
            largest = num  # update largest as current num
        elif num > second_largest and num != largest:
            second_largest = num  # update second_largest if num is larger than current second_largest and not equal to largest
    
    return second_largest