"""
QUESTION:
Implement the function `weighted_median(data, weights)` that calculates the weighted median of a list of numbers. The function takes two lists as input: `data` - a list of numbers, and `weights` - a list of weights corresponding to each number in the data list. The function should return the weighted median, which is the value that splits the list into two halves where the sum of the weights of the numbers less than the median is equal to the sum of the weights of the numbers greater than the median. The function should assume that the input lists are valid and of the same length.
"""

def weighted_median(data, weights):
    # Create a list of tuples (number, weight)
    weighted_data = list(zip(data, weights))

    # Sort the list of tuples based on numbers in ascending order
    weighted_data.sort(key=lambda x: x[0])

    # Calculate the total weight
    total_weight = sum(weights)

    # Iterate through the sorted list and calculate the cumulative weight
    cumulative_weight = 0
    for number, weight in weighted_data:
        cumulative_weight += weight
        if cumulative_weight >= total_weight / 2:
            return number

    # Return None if no weighted median is found
    return None