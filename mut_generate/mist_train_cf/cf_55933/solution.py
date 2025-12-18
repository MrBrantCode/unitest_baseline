"""
QUESTION:
Design a function called `analyze_array` that takes an array of numbers as input and returns the maximum number, the average value, and the count of numbers above the average. The array may contain both integers and floating point numbers. The function should handle potential errors such as an empty array or non-number elements, and return an error message if such cases occur.
"""

def analyze_array(arr):
    # Check if the array is empty
    if len(arr)==0:
        return "Error: Array is empty"
    
    # Initialize max, sum and count variables
    max_value = arr[0]
    total = 0
    count = 0

    # Iterate over the array
    for number in arr:
        # Check if the elements are numbers
        if isinstance(number, (int, float)):
            # If the number is greater than the current max, update max
            if number > max_value:
                max_value = number
            # Add the number to the total sum
            total += number
        else:
            return "Error: Array contains non-number elements"
        
    # Calculate the average
    average = total / len(arr)

    # Iterate over the array again to count elements above average
    for number in arr:
        if number > average:
            count += 1

    return max_value, average, count