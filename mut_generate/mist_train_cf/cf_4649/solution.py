"""
QUESTION:
Create a function named `modify_list` that takes a list of strings as input. The function should convert all elements to uppercase, remove duplicates, and sort the list in descending order. Then, it should print each element twice using a for loop. The function should have a time complexity of O(nlogn) and a space complexity of O(n).
"""

def modify_list(lst):
    # Convert all elements to uppercase
    lst = [element.upper() for element in lst]

    # Remove duplicates
    lst = list(set(lst))

    # Sort the list in descending order
    lst.sort(reverse=True)

    # Print each element twice using a for loop
    for element in lst:
        print(element)
        print(element)

    return lst