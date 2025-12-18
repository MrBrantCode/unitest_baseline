"""
QUESTION:
Create a function called `permutate_string` that takes a string as input and returns a list of all possible permutations of the string. If the length of the string is 1, the function should return a list containing the string itself. The function should not use any built-in permutation functions and should only use string slicing or substring methods to generate sub-strings.
"""

def permutate_string(string):
    """
    This function generates all possible permutations of the input string.
    
    Args:
    string (str): The string for which permutations are to be generated.
    
    Returns:
    list: A list of all possible permutations of the string.
    """
    
    # Base case: If the string length is 1, return a list containing the string itself.
    if len(string) == 1:
        return [string]
    
    # Initialize an empty list to store all permutations.
    permutations = []
    
    # Iterate over each character in the string.
    for index, char in enumerate(string):
        # Generate a sub-string by removing the current character from the original string.
        sub_string = string[:index] + string[index+1:]
        
        # Recursively call the permutate_string function with the sub-string.
        for perm in permutate_string(sub_string):
            # Append the current character at the start of each permutation and add to the permutations list.
            permutations.append(char + perm)
    
    # Return the list of all permutations.
    return permutations