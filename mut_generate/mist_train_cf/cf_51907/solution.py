"""
QUESTION:
Create a function named `find_numbers` that takes two parameters: `array` and `threshold`. This function should find all numbers in the `array` that are less than the given `threshold` and return these numbers along with their indices in the original `array`. The function should handle erroneous inputs and edge cases. The input `array` should be a list containing only integers or floats, and the `threshold` should be an integer or float. If the input is invalid or an error occurs, the function should return a relevant error message.
"""

def find_numbers(array, threshold):
    try:
        # check if input is a list
        if not isinstance(array, list):
            return "Error: input is not an array."
        
        # check if all elements in the list are int or float
        if not all(isinstance(i, (int, float)) for i in array):
            return "Error: input array contains non-numeric values."

        # check if threshold is int or float
        if not isinstance(threshold, (int, float)):
            return "Error: threshold is not a number."

        # check if array is empty
        if not array:
            return "Error: array is empty."

        result = [(i, idx) for idx, i in enumerate(array) if i < threshold]
        if not result:
            return "No number in the array is less than the threshold."

        return result

    except:
        return "An error occurred."