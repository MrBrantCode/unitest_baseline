"""
QUESTION:
Create a function `compare_arrays` that takes a list of arrays as input, compares the elements of the arrays, and returns a list of tuples containing the common elements and the number of arrays each element appears in. The arrays can have duplicate elements and contain integers ranging from -1000 to 1000, with a maximum of 20 elements per array.
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