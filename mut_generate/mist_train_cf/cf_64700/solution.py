"""
QUESTION:
Implement a function named `advanced_func` that takes a list as input and performs the following operations in order: 

- If an element is an integer, check if it is even, and if so, append '5' to it after increasing its value by 3. The result should be a string. 
- If an element is a float, subtract 3 from it if it is less than 10, otherwise divide it by 3. 
- If an element is a string, concatenate 'world' to it and convert the entire string to uppercase. 

The function should handle potential anomalies that might prevent successful execution, such as non-numeric strings, without using built-in functions to check the type of elements.
"""

def advanced_func(lst):
    for idx, element in enumerate(lst):
        try:
            if element % 1 == 0:
                if element % 2 == 0:
                    lst[idx] = str(element + 3) + '5'
                else:
                    lst[idx] = element
            else:
                if element < 10:
                    lst[idx] = element - 3
                else:
                    lst[idx] = element / 3
        except TypeError:
            if isinstance(element, str):
                lst[idx] = (element + 'world').upper()
                    
    return lst