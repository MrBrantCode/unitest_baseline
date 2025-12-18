"""
QUESTION:
Create a function named `insert_value` that takes in an array, a value, and a maximum length. The function should insert the value at the end of the array if the resulting array does not exceed the maximum length. If the array length exceeds the maximum length after insertion, remove the first element before inserting the new value. The function should not use any built-in Python methods such as `append`, `insert`, `pop`, `extend`, or `remove`.
"""

def insert_value(array, value, max_length):
    # Check if the array length exceeds the maximum length
    if len(array) >= max_length:
        # Remove the first element from the array
        array = array[1:]
    
    # Add the value at the end of the array
    # Note: Since we cannot use the append method, we will use the '+' operator to concatenate
    array = array + [value]
    
    return array