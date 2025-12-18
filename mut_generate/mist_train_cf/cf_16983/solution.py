"""
QUESTION:
Write a function named `count_specific_value` that takes two parameters: an array of integers and a specific integer value. The function should return the number of times the specific value exists in the array. The time complexity should be O(n) or better and the space complexity should be O(1), where n is the size of the array. The array size can be up to 10^9 and the elements can be any integer from -10^9 to 10^9.
"""

def count_specific_value(array, specific_value):
    count = 0
    for element in array:
        if element == specific_value:
            count += 1
    return count