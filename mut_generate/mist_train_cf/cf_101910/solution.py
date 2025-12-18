"""
QUESTION:
Write a function named `print_string` that takes a string as input and prints it to the console. The function should also measure and return the time it takes to print the string. Explore different formatting options such as font size and color that can be used when printing the string. The function should be optimized to handle large strings efficiently and minimize memory constraints.
"""

import time

def print_string(input_string):
    """
    Prints the input string to the console and returns the time it takes to print.
    
    Args:
        input_string (str): The string to be printed.
    
    Returns:
        float: The time it takes to print the string in seconds.
    """
    
    # Record the start time
    start_time = time.time()
    
    # Print the string with formatting options
    print("\033[1m\033[31m" + input_string + "\033[0m")
    
    # Record the end time and calculate the time taken
    end_time = time.time()
    time_taken = end_time - start_time
    
    return time_taken