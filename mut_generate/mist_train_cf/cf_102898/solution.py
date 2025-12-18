"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: an array of integers and a specific integer value. The function should return the number of occurrences of the specific value in the array. The array size can be up to 10^9 and the integers in the array and the specific value can range from -10^9 to 10^9. The function should have a time complexity of O(n) or better.
"""

def count_occurrences(arr, specific_value):
    count = 0
    for element in arr:
        if element == specific_value:
            count += 1
    return count