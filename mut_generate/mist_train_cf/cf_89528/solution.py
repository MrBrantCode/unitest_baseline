"""
QUESTION:
Create a function named `sum_arrays` that takes two arrays of integers `arr1` and `arr2` as input and returns a new array of integers. The new array should contain the sum of corresponding elements of `arr1` and `arr2`. If `arr1` is longer than `arr2`, append the remaining elements of `arr1` to the new array. If `arr2` is longer than `arr1`, append the remaining elements of `arr2` to the new array. Ensure that the sum of each pair of corresponding elements does not exceed 100, and the sum of all elements in the new array does not exceed 1000.
"""

def sum_arrays(arr1, arr2):
    # Find the lengths of the two arrays
    len1 = len(arr1)
    len2 = len(arr2)
    
    # Find the minimum length between the two arrays
    min_len = min(len1, len2)
    
    # Create an empty array to store the sums
    new_array = []
    
    # Iterate through the elements of the arrays up to the minimum length
    for i in range(min_len):
        # Find the sum of the corresponding elements and append it to the new array
        new_element = arr1[i] + arr2[i]
        new_array.append(min(100, new_element))
        
    # Check if arr1 has remaining elements
    if len1 > len2:
        # Iterate through the remaining elements of arr1
        for i in range(min_len, len1):
            # Append the remaining elements to the new array
            new_element = min(100, arr1[i])
            
            # Check if the sum of all elements in the new array exceeds 1000
            if sum(new_array) + new_element > 1000:
                break
            
            new_array.append(new_element)
    
    # Check if arr2 has remaining elements
    if len2 > len1:
        # Iterate through the remaining elements of arr2
        for i in range(min_len, len2):
            # Append the remaining elements to the new array
            new_element = min(100, arr2[i])
            
            # Check if the sum of all elements in the new array exceeds 1000
            if sum(new_array) + new_element > 1000:
                break
            
            new_array.append(new_element)
    
    return new_array