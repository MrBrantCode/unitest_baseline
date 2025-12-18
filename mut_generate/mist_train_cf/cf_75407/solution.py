"""
QUESTION:
Create a function `transform_component` that takes a list, an index, and a transformation function as arguments. The function should apply the transformation function to the element at the given index within the list and return the transformed list. If the index is out of bounds, handle the error accordingly.
"""

def transform_component(input_list, index, transformation):
    """
    This function takes an input list, an index, and a transformation function as arguments,
    applies the transformation function to the element at the given index within the list, 
    and returns the transformed list.
    """
    try:
        input_list[index] = transformation(input_list[index])
    except IndexError:
        print("Error: Index is out of bounds")
    except Exception as e:
        print("An error occurred: ", e)

    return input_list