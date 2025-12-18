"""
QUESTION:
Create a function `print_collection_elements` that takes a list of integers as input. The function should iterate through the list, print the index and value of each element, and determine if the element is even or odd without using built-in functions or methods. If an element is even, it should be appended to a separate list. The function should then return the list of even elements. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the input list.
"""

def print_collection_elements(collection):
    """
    This function prints the index and value of each element in the input list, 
    determines if the element is even or odd, and returns a list of even elements.

    Args:
        collection (list): A list of integers.

    Returns:
        list: A list of even integers from the input list.
    """
    even_elements = []
    for index, element in enumerate(collection):
        print(f"Index: {index}, Element: {element}")
        if element // 2 * 2 == element:
            print("Even")
            even_elements.append(element)
        else:
            print("Odd")
    return even_elements