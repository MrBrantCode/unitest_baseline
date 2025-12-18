"""
QUESTION:
Create a function `find_min(array)` that takes a list of elements as input and returns the least numerical value in the list. If the input is not a list, the function should return an error message. The function should also handle non-numeric values in the list and return an error message if detected. If the list does not contain any numeric values, the function should return a message indicating this.
"""

def find_min(array):
  try:
    # Check if input is a list
    if not isinstance(array, list):
        return "Input should be a list."
    
    min_val = None
    for i in array:
        # Check if item is a number
        if isinstance(i, (int,float)):
            if min_val is None or i < min_val:
                min_val = i
        else:
            return "Non-numeric value detected in array."

    # If no numeric values in list
    if min_val is None:
        return "List contains no numeric values."
    else:
        return min_val

  except Exception as e:
    return str(e)