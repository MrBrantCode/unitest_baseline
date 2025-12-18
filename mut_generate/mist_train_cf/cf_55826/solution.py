"""
QUESTION:
Implement a function `advanced_func` that takes a list as input and performs the following operations: 
- Appends '5' to every integer within the list 
- Subtracts '3' from every float value
- Concatenates 'world' to every string present in the list

The function should maintain the order of transformations as specified and handle any anomalies that could affect successful execution. 
Do not use built-in functions like `type()` to check the data type of elements. 
Test the function with the input `[1, 2, "hello", 1.5, "earth"]`.
"""

def advanced_func(lst):
    res_lst = []
 
    for element in lst:
        if isinstance(element, int):
            res_lst.append(element + 5)
        elif isinstance(element, float):
            res_lst.append(element - 3)
        elif isinstance(element, str):
            res_lst.append(element + 'world')
        else:
            print(f"Anomaly detected: Element {element} of type {type(element)} can't be processed")

    return res_lst