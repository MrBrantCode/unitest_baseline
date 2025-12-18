"""
QUESTION:
Create a function named `count_string_occurrences` that accepts two parameters: a string and a list of strings. The function should return a dictionary where the keys are the unique strings from both the input string and the list, and the values are the number of occurrences of each string. The function should ignore case sensitivity, consider all words separated by whitespace as separate strings, and handle duplicate strings correctly.
"""

def count_string_occurrences(string, string_list):
    # Convert the input string to lowercase and split it into individual words
    words = string.lower().split()
    
    # Create an empty dictionary to store the occurrences
    occurrences = {}
    
    # Loop through each word in the list of words
    for word in words + [s.lower() for s in string_list]:
        # Check if the word is already in the occurrences dictionary
        if word in occurrences:
            # If it is, increment its count by 1
            occurrences[word] += 1
        else:
            # If it is not, add it to the occurrences dictionary with a count of 1
            occurrences[word] = 1
    
    return occurrences