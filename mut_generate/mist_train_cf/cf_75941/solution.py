"""
QUESTION:
Write a function named `modulo_tuples` that takes two lists of tuples as input. The function should perform an element-wise modulo operation on the tuples and return the result as a new list of tuples. The function should handle cases where the input lists are of different lengths, the input elements are not tuples, the tuples are of different lengths, the elements of the tuples are not integers, and division by zero. In such cases, the function should return an error message. The function should be optimized for large inputs.
"""

def modulo_tuples(list1, list2):
    # Check if both lists are of the same length
    if len(list1) != len(list2):
        return "Error: Lists are of different lengths."
        
    result = []
    
    for tup1, tup2 in zip(list1, list2):
        # Check if both elements are tuples
        if not isinstance(tup1, tuple) or not isinstance(tup2, tuple):
            return "Error: One or more elements is not a tuple."
            
        # Check if both tuples are of the same length
        if len(tup1) != len(tup2):
            return "Error: Tuples are of different lengths."
            
        temp_result = []
        for num1, num2 in zip(tup1, tup2):
            # Check if both elements are integers
            if not isinstance(num1, int) or not isinstance(num2, int):
                return "Error: One or more elements is not an integer."
                
            # Check if second number is not zero
            if num2 == 0:
                return "Error: Cannot divide by zero."
                    
            temp_result.append(num1 % num2)
            
        result.append(tuple(temp_result))
            
    return result