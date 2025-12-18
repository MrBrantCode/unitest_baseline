"""
QUESTION:
Implement a function named `calculate_percentages` that takes a list of elements as input. The function should return a dictionary where the keys are the unique elements from the input list, and the values are the percentages of occurrences of each element in the input list, rounded to two decimal places.
"""

def calculate_percentages(input_list):
    counts = {}
    percentages = {}
    total_elements = len(input_list)

    # Count occurrences of each element
    for element in input_list:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    # Calculate percentages
    for key, value in counts.items():
        percentages[key] = round((value / total_elements) * 100, 2)

    return percentages