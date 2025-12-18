"""
QUESTION:
Create a function `call_by_value(num)` and `call_by_reference(data_structure)` that demonstrate the difference between call by value and call by reference in programming. The `call_by_value(num)` function should take a number as an argument, increment it by 10, and return the result without modifying the original number. The `call_by_reference(data_structure)` function should take a mutable data structure (such as a list or dictionary) as an argument, modify it, and return the modified data structure. Implement both functions in Python and provide examples to illustrate the difference between call by value and call by reference.
"""

def call_by_value(num):
    num += 10
    return num

def call_by_reference(data_structure):
    data_structure.append(" World")
    return data_structure