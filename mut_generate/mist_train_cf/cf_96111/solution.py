"""
QUESTION:
Create a function `detect_duplicates` that takes an array of elements as input and returns the frequency of each duplicate element. The function should be able to handle arrays of up to 10^6 elements, including negative numbers and floating-point numbers. The function should achieve an average time complexity of O(n) and space complexity of O(k), where n is the length of the input array and k is the number of unique elements in the array.

The function should return the frequency of each duplicate element in the array.
"""

from collections import defaultdict

def detect_duplicates(arr):
    """
    This function takes an array of elements as input and returns the frequency of each duplicate element.
    
    Parameters:
    arr (list): The input array containing elements of any data type.
    
    Returns:
    dict: A dictionary containing the frequency of each duplicate element.
    """
    hash_table = defaultdict(int)
    
    for element in arr:
        if element not in hash_table:
            hash_table[element] = 1
        else:
            hash_table[element] += 1
    
    duplicates = {element: frequency for element, frequency in hash_table.items() if frequency > 1}
    
    return duplicates