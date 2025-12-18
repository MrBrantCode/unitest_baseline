"""
QUESTION:
Develop a function called `convert_to_integer` that takes an array of real numbers and returns a new array with the numbers rounded to the nearest integer. The function should round up if the decimal part is greater than 0.5 and round down if it is less than or equal to 0.5. The function should have a time complexity of O(n) and handle errors by returning an error message if the input array is empty or contains non-numeric values.
"""

def convert_to_integer(arr):
    if len(arr) == 0:
        return "Input array is empty"
    
    try:
        result = []
        for num in arr:
            if isinstance(num, (int, float)):
                result.append(int(num + 0.5))  
            else:
                return "Input array contains non-numeric values"
        
        return result
    
    except Exception as e:
        return str(e)