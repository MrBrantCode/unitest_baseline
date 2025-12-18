"""
QUESTION:
Write a function called `extract_first_three_unique_elements` that takes a list as input and returns the first three unique elements from the list. The function should not use built-in slicing and should handle duplicate elements in the list. The output list should contain unique elements only, in the order they appear in the input list.
"""

def extract_first_three_unique_elements(lst):
    extracted = []
    unique_elements = set()
    
    for element in lst:
        if element not in unique_elements:
            extracted.append(element)
            unique_elements.add(element)
            
        if len(extracted) == 3:
            break
    
    return extracted