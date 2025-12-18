"""
QUESTION:
Create a function called `print_odd_integers` that takes a potentially nested list of integers as input. This function should recursively traverse the list, printing only the odd integers it encounters. The function should also handle non-list inputs and non-integer values within the list by printing an error message.
"""

def entrance(data):
    if not isinstance(data, list):
        print(f"Input is not an array: {data}")
        return
    
    for item in data:
        if isinstance(item, list):
            entrance(item)
        elif isinstance(item, int):
            if item % 2 != 0:
                print(item)
        else:
            print(f"Non-integer value in the array: {item}")