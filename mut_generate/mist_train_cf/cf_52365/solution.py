"""
QUESTION:
Write a function named `find_largest_and_second_largest` that finds the largest and second largest values in an array of numbers without using any in-built sort or max functions. The function should take an array of numbers as input and return the largest and second largest numbers. The function should be efficient and have a time complexity of O(n), where n is the length of the array.
"""

def find_largest_and_second_largest(arr):
    num1 = num2 = float('-inf')
    for num in arr:
        if num > num1:
            num2 = num1
            num1 = num
        elif num > num2 and num != num1:
            num2 = num
    return num1, num2