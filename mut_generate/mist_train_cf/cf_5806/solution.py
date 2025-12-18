"""
QUESTION:
Create a function called `find_duplicates` that takes an array of elements as input and returns the frequency of each duplicate element in the array. The array can contain a maximum of 10^9 elements, including negative numbers and floating-point numbers. The function should have an average time complexity of O(n log n) and a space complexity of O(n), where n is the length of the input array.
"""

from collections import defaultdict

def find_duplicates(arr):
    """
    This function takes an array of elements as input and returns the frequency of each duplicate element in the array.
    
    Parameters:
    arr (list): The input array containing elements of any type.
    
    Returns:
    dict: A dictionary containing the frequency of each duplicate element in the array.
    """
    hash_table = defaultdict(int)
    
    for element in arr:
        hash_table[element] += 1
    
    duplicates = {element: frequency for element, frequency in hash_table.items() if frequency > 1}
    
    return duplicates