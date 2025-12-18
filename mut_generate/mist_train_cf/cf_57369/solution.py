"""
QUESTION:
Design a function `insert_element` that takes a list, an index, and an element as arguments. The function should insert the element at the specified index in the list and maintain the list in ascending order. If the input index is not an integer, the function should return an error message. If the input index is out of the list's range, the function should catch the error and return an appropriate error message. The function should also handle any other unforeseen exceptions by returning an error message.
"""

def insert_element(lst, index, element):
    try:
        if isinstance(index, int):
            lst.insert(index, element)
            lst.sort()
            return lst
        else:
            return "Error: Index must be an integer."
    except IndexError:
        return "Error: Index is out of range."
    except Exception as e:
        return "An unexpected error occurred. Error message: " + str(e)