"""
QUESTION:
Create a function named `count_string_occurrences` that takes two parameters: `string` and `string_list`. The function should return a dictionary where the keys are the unique strings from both the input `string` and `string_list`, and the values are the number of occurrences of each string. The function should ignore case sensitivity, consider all words separated by whitespace as separate strings, and count duplicate strings correctly. The input `string` should only contain alphabetical characters and whitespace, and `string_list` should have a maximum length of 1000 with each string having a maximum length of 100 characters.
"""

def count_string_occurrences(string, string_list):
    """
    Returns a dictionary with unique strings from both the input string and string_list,
    and their corresponding occurrences. The function is case-insensitive.

    Parameters:
    string (str): Input string containing alphabetical characters and whitespace.
    string_list (list): List of strings with a maximum length of 1000 and each string having a maximum length of 100 characters.

    Returns:
    dict: Dictionary with unique strings as keys and their occurrences as values.
    """

    # Convert the input string to lowercase
    string = string.lower()
    
    # Create an empty dictionary to store the occurrences
    occurrences = {}
    
    # Split the input string into individual words
    words = string.split()
    
    # Loop through each word in the list
    for word in words:
        # Check if the word is already in the occurrences dictionary
        if word in occurrences:
            # If it is, increment its count by 1
            occurrences[word] += 1
        else:
            # If it is not, add it to the occurrences dictionary with a count of 1
            occurrences[word] = 1
    
    # Loop through each string in the string_list
    for string in string_list:
        # Convert the string to lowercase
        string = string.lower()
        
        # Check if the string is already in the occurrences dictionary
        if string in occurrences:
            # If it is, increment its count by 1
            occurrences[string] += 1
        else:
            # If it is not, add it to the occurrences dictionary with a count of 1
            occurrences[string] = 1
    
    return occurrences