"""
QUESTION:
Implement a function `calculate` that takes a list of numbers as input and returns a dictionary with the count, sum, average, minimum, and maximum of the numbers greater than 6. The function should handle empty lists, non-numeric values, and other potential errors, and return error messages accordingly.
"""

def calculate(arr):
    try:
        if not all(isinstance(i, (int, float)) for i in arr):
            return "All elements in the array must be integers or floats."
        
        if len(arr) == 0:
            return "The array is empty."
        
        greater_than_six = [i for i in arr if i > 6]
        
        if len(greater_than_six) == 0:
            return "There are no elements greater than 6 in the array."
        
        count = len(greater_than_six)
        total_sum = sum(greater_than_six)
        avg = total_sum / count
        minimum = min(greater_than_six)
        maximum = max(greater_than_six)
        
        return {"count": count, 
                "sum": total_sum, 
                "average": avg, 
                "min": minimum, 
                "max": maximum}
    except Exception as e:
        return f"An error occurred: {e}"