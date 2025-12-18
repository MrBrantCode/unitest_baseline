"""
QUESTION:
Create a function `compare_arrays` that takes a list of at most 10 arrays as input. Each array contains at most 20 integer elements ranging from -1000 to 1000 and may include duplicates. The function should return a list of tuples, where each tuple contains an integer and the number of arrays it appears in. The function should only include integers that appear in all input arrays.
"""

def compare_arrays(arrays):
    common_elements = {}
    
    for array in arrays:
        unique_elements = set(array)
        
        for element in unique_elements:
            if element in common_elements:
                common_elements[element] += 1
            else:
                common_elements[element] = 1
    
    result = []
    for element, count in common_elements.items():
        if count == len(arrays):
            result.append((element, count))
    
    return result