"""
QUESTION:
Implement a function named `find_element` that uses a 'break' statement within a nested loop structure to search for a specified element within a multi-dimensional array. The function should take two parameters: `data` (the multi-dimensional array) and `value` (the element to be searched). The function should print the position of the element if found and return, otherwise it should print a message indicating that the element was not found.
"""

def find_element(data, value):
    # Iterating over the outer loop
    for i, sublist in enumerate(data):
        # Iterating over the inner loop
        for j, element in enumerate(sublist):
            # If the element is found, print its position and break
            if element == value:
                print(f"Found {value} at data[{i}][{j}]")
                return
    print(f"{value} not found in array")