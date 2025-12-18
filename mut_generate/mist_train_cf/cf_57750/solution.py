"""
QUESTION:
Create a function called `intricate_frequency_analyzer` that takes a string composed of space-separated characters, including uppercase and lowercase alphabets, numeric characters, and punctuation. The function should return a dictionary featuring the highest frequency character(s), with alphabets in lowercase, followed by their count. If multiple characters have the same highest frequency, return all of them. The function should ignore case sensitivity for alphabets.
"""

def intricate_frequency_analyzer(test):
    """
    Analyzes the frequency of characters in a given string and returns a dictionary
    featuring the highest frequency character(s) in lowercase, followed by their count.
    
    Args:
        test (str): The input string to be analyzed.
    
    Returns:
        dict: A dictionary containing the highest frequency character(s) and their count.
    """

    # Initialize an empty dictionary to store character frequencies
    tally = {}
    
    # Initialize a variable to keep track of the maximum frequency
    max_count = 0
    
    # Iterate over each character in the input string
    for chartype in test:
        # Ignore spaces
        if chartype != ' ':
            # Convert alphabets to lowercase for case-insensitive counting
            if chartype.lower() in tally:
                # Increment the count if the character is already in the dictionary
                tally[chartype.lower()] += 1
            else:
                # Add the character to the dictionary with a count of 1
                tally[chartype.lower()] = 1
                
            # Update the maximum frequency if the current character's frequency is higher
            if tally[chartype.lower()] > max_count:
                max_count = tally[chartype.lower()]
                
    # Filter the dictionary to only include characters with the highest frequency
    result = {char: count for char, count in tally.items() if count == max_count}
    
    return result