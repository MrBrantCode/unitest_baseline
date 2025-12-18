"""
QUESTION:
Write a function `find_element(array, element)` that takes a nested array and an element as input and prints the index position of the element if found, or a message stating that the element is not present. The index position should be printed in the format [outer index][inner index] if the element is in a nested list, or [outer index] if the element is directly in the outer array.
"""

def find_element(array, element):
    for i in range(len(array)):
        if type(array[i]) == list:
            for j in range(len(array[i])):
                if array[i][j] == element:
                    print(f"Element '{element}' found at index [{i}][{j}]")
                    return
        elif array[i] == element:
            print(f"Element '{element}' found at index [{i}]")
            return
    
    print(f"Element '{element}' is not present")