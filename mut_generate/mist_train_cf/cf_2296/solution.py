"""
QUESTION:
Write a function `calculate_mode(strings)` that calculates the mode of a given list of strings. The mode is the string(s) that appear(s) most frequently in the list. If multiple strings have the same highest frequency, return all of them. The list may contain duplicate strings and empty strings. The function should not use any built-in functions or libraries for counting frequencies or sorting the list, and should only use arrays and basic array operations.
"""

def calculate_mode(strings):
    # Initialize variables to store the mode and its frequency
    mode = []
    max_frequency = 0
    
    # Iterate over each string in the list
    for i in range(len(strings)):
        frequency = 0
        
        # Skip empty strings
        if strings[i] == "":
            continue
        
        # Iterate over the rest of the list to count the frequency of the current string
        for j in range(i, len(strings)):
            if strings[i] == strings[j]:
                frequency += 1
        
        # If the frequency of the current string is higher than the previous maximum frequency,
        # update the mode and the maximum frequency
        if frequency > max_frequency:
            mode = [strings[i]]
            max_frequency = frequency
        # If the frequency is equal to the previous maximum frequency, add the string to the mode
        elif frequency == max_frequency:
            mode.append(strings[i])
    
    return mode