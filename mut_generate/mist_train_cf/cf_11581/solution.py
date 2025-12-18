"""
QUESTION:
Function Name: convert_string_to_array

The function should take a string as input, remove leading and trailing spaces, and convert it into a sorted array of unique integers. The string may contain multiple consecutive commas, non-numeric characters, and negative numbers. The function should treat multiple consecutive commas as empty elements, ignore non-numeric characters, and consider negative numbers as valid elements. The array should not contain any duplicate elements and should be sorted in ascending order.
"""

def convert_string_to_array(string):
    """
    This function takes a string as input, removes leading and trailing spaces, 
    and converts it into a sorted array of unique integers.

    Args:
        string (str): The input string containing integers separated by commas.

    Returns:
        list: A sorted list of unique integers.
    """
    
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Split the string into elements using commas as separators
    elements = string.split(",")
    
    # Initialize an empty list to store valid numbers
    numbers = []
    
    # Iterate through each element
    for element in elements:
        # Remove leading and trailing spaces from each element
        element = element.strip()
        
        # Check if the element is not empty and is numeric (including negative numbers)
        if element != "" and element.lstrip('-').isdigit():
            # Convert the element to an integer
            number = int(element)
            
            # Check if the number is already in the list
            if number not in numbers:
                # Add the number to the list
                numbers.append(number)
    
    # Sort the list in ascending order
    numbers.sort()
    
    return numbers