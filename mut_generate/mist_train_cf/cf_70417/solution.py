"""
QUESTION:
Write a function `higher_frequency_elements` that takes a list of positive integers as input and returns a list containing the average of all distinct elements whose occurrence frequency is greater than half of the unique elements in the list. If no such elements exist, return an empty list and an error message.
"""

from collections import Counter

def higher_frequency_elements(data_structure):
    unique_elements_count = len(set(data_structure))
    half_unique_elements_count = unique_elements_count / 2
    
    freq_counter = Counter(data_structure)
    
    result = [elem for elem, count in freq_counter.items() if count > half_unique_elements_count]
    
    if result:
        avg = sum(result) / len(result)
        return [avg]
    else:
        return [], 'No elements with frequency higher than half of the unique elements'