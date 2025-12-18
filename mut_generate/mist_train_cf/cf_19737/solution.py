"""
QUESTION:
Create a function named `print_string_with_list` that takes three parameters: `string`, `integer`, and `list`. The function should print the `string` the given `integer` number of times. Each printed string should be appended with a character from the `string` based on the corresponding index value in the `list`. The `string` must contain at least 5 characters, the `integer` must be within the range of 1 to 10, and the `list` must contain exactly the same number of elements as the `integer` value.
"""

def print_string_with_list(string, integer, list):
    """
    Prints the given string a specified number of times, 
    appending a character from the string based on the corresponding index value in the list.

    Args:
        string (str): The string to be printed.
        integer (int): The number of times the string is printed.
        list (list): A list of index values.

    Returns:
        None
    """

    # Check if the string has at least 5 characters
    if len(string) < 5:
        print("Error: String must contain at least 5 characters")
        return

    # Check if the integer is within the range of 1 to 10
    if integer < 1 or integer > 10:
        print("Error: Integer must be within the range of 1 to 10")
        return

    # Check if the list has the same number of elements as the integer value
    if len(list) != integer:
        print("Error: List must contain exactly the same number of elements as the integer value")
        return

    # Print the string with the corresponding character appended
    for i in range(integer):
        print(string + string[list[i]])