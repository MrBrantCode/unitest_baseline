"""
QUESTION:
Write a function named `count_specific_value` that takes two parameters: an array of integers and a specific integer value. The function should count the occurrences of the specific value in the array and return the count. The space complexity should be O(1) and the time complexity should be O(n) or better. The array can have up to 10^9 elements, and the elements and specific value can be any integer from -10^9 to 10^9.
"""

def count_specific_value(array, specific_value):
    count = 0
    for element in array:
        if element == specific_value:
            count += 1
    return count