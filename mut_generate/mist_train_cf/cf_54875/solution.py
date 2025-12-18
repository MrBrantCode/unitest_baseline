"""
QUESTION:
Create a function called `sort_complex_numbers` that sorts an array of complex numbers based on the prevalence of their real parts. The function should return the sorted array. If two or more real parts have the same prevalence, the corresponding complex numbers should be sorted by their real part values. The function should take an array of complex numbers as input and does not have any other restrictions on the input.
"""

def sort_complex_numbers(items):
    """
    Sorts an array of complex numbers based on the prevalence of their real parts.
    
    If two or more real parts have the same prevalence, the corresponding complex numbers 
    are sorted by their real part values.

    Args:
        items (list): A list of complex numbers.

    Returns:
        list: The sorted list of complex numbers.
    """
    # Create a dictionary where key is real part and value is its count
    count_dict = {item.real: sum(1 for i in items if i.real==item.real) for item in items}

    # Sort array based on count of real part. If counts are equal, sort based on real part.
    items.sort(key=lambda x: (-count_dict[x.real], x.real))
    return items