"""
QUESTION:
Create a function named `assign_variables(number)` that generates a string containing a name and age based on the provided number. The name should be selected from a predefined list, and the index of the name in the list should be determined by the number (using modulus operation to ensure the index is within bounds). The age should be the number itself. The string should be formatted as "Name: {}, Age: {}".
"""

def assign_variables(number):
    names = ["John", "Bob", "Alice", "Mary", "James", "Jennifer", "Michael", "Jessica", "Jacob", "Emma"]
    name = names[number % len(names)]    # Get a name from the list based on the number
    age = number                         # Use the number itself as the age
    variable_string = 'Name: {}, Age: {}'.format(name, age) # Format the string
    return variable_string