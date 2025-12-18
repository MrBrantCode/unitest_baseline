"""
QUESTION:
Construct a function named `pairwise_modulo` that accepts two lists of tuples of identical length. The function must perform an element-wise modulo operation on corresponding tuples from the two lists and return a new list of tuples containing the results. 

The function should return an error message in the following scenarios:
- The inputs are not lists
- The lists are not of the same length
- The elements of the lists are not tuples
- The tuples contain non-integer values
- The tuples are not of the same length
- A tuple in the second list contains a zero value, which would result in a division by zero error during the modulo operation.

The function should be designed to efficiently process large inputs.
"""

def pairwise_modulo(tuples1, tuples2):
    
    # Check if both inputs are lists
    if not isinstance(tuples1, list) or not isinstance(tuples2, list):
        return "Error: Both inputs should be lists."
        
    # Check if both lists are of same length
    if len(tuples1) != len(tuples2):
        return "Error: Both lists should be of same length."
    
    # Check if all elements of both lists are tuples of integers
    for t in tuples1+tuples2:
        if not isinstance(t, tuple):
            return "Error: All elements of input lists should be tuples."
        if not all(isinstance(i, int) for i in t):
            return "Error: All elements of the tuples should be integers."
    
    result = []
    
    for pair1, pair2 in zip(tuples1, tuples2):
        
        # Check if both tuples are of same length
        if len(pair1) != len(pair2):
            return "Error: Corresponding tuples should be of same length."
        
        temp = []
        
        for a, b in zip(pair1, pair2):
            if b == 0:    # handle division by zero
                return "Error: Cannot perform modulo operation with denominator zero."
            temp.append(a % b)  # add modulo result to temporary list
            
        result.append( tuple(temp) )    # add tuple to result
    
    return result