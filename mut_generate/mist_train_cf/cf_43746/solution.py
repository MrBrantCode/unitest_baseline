"""
QUESTION:
Write a function named `filter_values` that takes a string of comma-separated values as input. The function should filter out non-numerical values, find the highest numerical value, and return three values: a string of the remaining numerical values (joined by commas), a string of the filtered non-numerical values (joined by commas), and the highest numerical value. Treat any value that is not purely a number as a non-numerical value.
"""

def filter_values(input_string):
    all_values = input_string.split(',')
    numerical_values = []
    non_numerical_values = []
    
    for value in all_values:
        # strip leading and trailing white spaces
        value = value.strip()
        # check if the value is numerical by trying to convert to integer
        try:
            numerical_values.append(int(value))
        except ValueError:
            non_numerical_values.append(value)

    # join back the values into string using comma
    numerical_string = ', '.join(map(str, numerical_values))
    non_numerical_string = ', '.join(non_numerical_values)

    max_value = max(numerical_values)

    return numerical_string, non_numerical_string, max_value