"""
QUESTION:
Create a function named `convert_to_integer` that takes an array of real numbers as input and returns a new array with each real number converted to its nearest integer value. The conversion should round up the values if they are greater than 0.5 and round down if they are less than or equal to 0.5. The function must have a time complexity of O(n), where n is the length of the input array, and handle errors gracefully by returning an error message if the input array is empty or contains non-numeric values.
"""

def convert_to_integer(arr):
    if len(arr) == 0:
        return "Input array is empty"
    
    try:
        result = []
        for num in arr:
            if isinstance(num, (int, float)):
                if num > 0.5:
                    result.append(int(num + 1) if num % 1 > 0.5 else int(num))
                else:
                    result.append(int(num))
            else:
                return "Input array contains non-numeric values"
        
        return result
    
    except Exception as e:
        return str(e)