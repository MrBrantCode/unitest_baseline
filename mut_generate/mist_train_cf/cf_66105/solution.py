"""
QUESTION:
Create a function called `inverted_array_and_inversions` that takes a list of integers as input and returns a tuple containing two values: the input list in reverse order and the count of inversions in the original list. An inversion is a pair of elements A and B where A > B and A appears before B in the list.
"""

def inverted_array_and_inversions(input_array):
    # Generate the inversely ordered array
    inverted_array = list(reversed(input_array))
    
    # Count the inversions in the original array
    inversion_count = 0
    for i in range(len(input_array)):
        for j in range(i+1,len(input_array)):
            if input_array[i] > input_array[j]:
                inversion_count += 1
                
    return inverted_array, inversion_count