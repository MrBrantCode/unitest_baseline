"""
QUESTION:
Design a function named `process_strings` that takes a list of strings as input. The function should remove strings containing the phrase "regardless of" and count the frequency of strings where this phrase appears more than once. It should return a new sorted list of strings that didn't contain the phrase "regardless of", sorted in descending order based on their lengths, along with the frequency count.
"""

def process_strings(lst):
    new_list = []
    counter = 0

    # Iterate over each string in the list of strings
    for string in lst:
        # Check how many times the phrase "regardless of" appears in the string
        count = string.count("regardless of")

        # If the phrase didn't appear in the string, append it to the new list
        if count == 0:
            new_list.append(string)
        elif count > 1:
            # If the phrase appeared more than once, increment the counter
            counter += 1

    # Sort the new list in descending order of string length
    new_list.sort(key=len, reverse=True)

    return new_list, counter