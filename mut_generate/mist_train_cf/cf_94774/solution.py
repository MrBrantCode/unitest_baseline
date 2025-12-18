"""
QUESTION:
Create a function called `process_strings` that takes a list of strings as input. The function should return a new list of strings that only includes strings from the input list that are all letters, have a length of at least 5, and have been converted to uppercase. The output list should have no duplicates and be sorted in descending order by string length. If the input list is empty or contains only invalid strings, return the message "Input list is empty" or "No valid strings found", respectively.
"""

def process_strings(strings):
    # Check if the input list is empty
    if not strings:
        return "Input list is empty"
    
    processed_strings = []
    
    for string in strings:
        # Check if the string contains numbers or special characters
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue  # Ignore the string
            
        # Convert the string to uppercase
        upper_string = string.upper()
        
        # Check if the length of the string is greater than or equal to 5
        if len(upper_string) >= 5:
            processed_strings.append(upper_string)
    
    # Check if all the strings were ignored
    if not processed_strings:
        return "No valid strings found"
    
    # Remove duplicate strings and sort the strings in descending order based on their length
    return sorted(set(processed_strings), key=len, reverse=True)