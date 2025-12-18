"""
QUESTION:
Write a function `smallest_abs_val` that takes a list of mixed data types as input and returns the smallest absolute value of the numeric elements. The function should exclude non-numeric elements (e.g., strings) and handle exceptions. If the list does not contain any numeric elements, the function should return `None`.
"""

def smallest_abs_val(input_list):
    """
    This function takes a list of mixed data types as input, 
    and returns the smallest absolute value of the numeric elements.

    Args:
    input_list (list): A list containing mixed data types.

    Returns:
    float or int: The smallest absolute value of the numeric elements.
    None: If the list does not contain any numeric elements.
    """
    
    try:
        nums = [abs(num) for num in input_list if type(num) == float or type(num) == int]
        if len(nums) == 0:
            return None
        else:
            return min(nums)
    except ValueError:
        print("Error: List contains invalid values.")
    except Exception as e:
        print(f"An error occurred: {e}")