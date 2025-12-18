"""
QUESTION:
Create a function called `count_duplicates` that takes a list of elements as input and returns a dictionary where the keys are the duplicate elements from the list and the values are their respective counts, excluding non-duplicate elements from the output.
"""

def count_duplicates(lst):
    duplicates = {}
    for element in lst:
        if element in duplicates:
            duplicates[element] += 1
        else:
            duplicates[element] = 1
            
    duplicates = {key: value for key, value in duplicates.items() if value > 1}
    
    return duplicates