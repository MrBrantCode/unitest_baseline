"""
QUESTION:
Develop a function called `convert_to_integers` that takes an array of values as input. The function should round each numeric value in the array to its nearest integer, rounding up if the decimal value is greater than 0.5 and rounding down if it is less than or equal to 0.5. If the input array contains any non-numeric values, the function should return an error message indicating which values are non-numeric. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def convert_to_integers(arr):
    result = []
    non_numeric_values = []
    
    for num in arr:
        if isinstance(num, (int, float)):
            if num % 1 >= 0.5:
                result.append(int(num + 0.5))
            else:
                result.append(int(num))
        else:
            non_numeric_values.append(str(num))
    
    if non_numeric_values:
        return "Error: The following values are non-numeric - " + ", ".join(val for val in non_numeric_values)
    
    return result