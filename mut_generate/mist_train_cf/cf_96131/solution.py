"""
QUESTION:
Write a function `find_duplicates` that takes an array of integers as input and returns an array of duplicates in descending order. The input array may contain up to 10^9 elements, where each integer is between 1 and 10^6, inclusive. A duplicate is defined as an integer that appears more than once in the input array.
"""

def find_duplicates(arr):
    freq_dict = {}
    duplicates = []
    
    # Count the frequency of each element in the array
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Check which elements have a frequency greater than 1
    for num, freq in freq_dict.items():
        if freq > 1:
            duplicates.append(num)
    
    # Sort the duplicates in descending order
    duplicates.sort(reverse=True)
    
    return duplicates