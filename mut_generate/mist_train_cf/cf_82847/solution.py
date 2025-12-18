"""
QUESTION:
Implement a recursive Python function named `extract_unique_elements` that takes a JSON object `data` as input and returns unique elements within nested arrays without duplicates, prioritizing elements from the topmost level of the nested arrays. The function should also identify and print the type of pattern (arithmetic, geometric, or none) among the unique elements.
"""

import json

def find_pattern(lst):
    if isinstance(lst, list) and len(lst) > 1:
        # Check for arithmetic pattern
        if len(set([lst[i] - lst[i - 1] for i in range(1, len(lst))])) == 1:
            return 'arithmetic'

        # Check for geometric pattern
        if len(set([lst[i] / lst[i - 1] for i in range(1, len(lst)) if lst[i - 1] != 0])) == 1:
            return 'geometric'

    return 'none'

def extract_unique_elements(data):
    unique_elements = []
    
    def extract(data):
        if isinstance(data, list):
            for item in data:
                if isinstance(item, list):
                    extract(item)
                elif item not in unique_elements:
                    unique_elements.append(item)

        elif isinstance(data, dict):
            for value in data.values():
                extract(value)

    extract(data)
    print('Unique elements:', unique_elements)
    print('Pattern:', find_pattern(unique_elements))