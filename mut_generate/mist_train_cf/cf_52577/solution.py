"""
QUESTION:
Write a function `even_characters` that takes a list of strings as input and returns a list of strings. Each output string should contain the count of even characters and the count of numerical elements in the corresponding input string, in the format "The number of even characters in the i'th input string is j, and the number of numericals is k." where i is the 1-based index of the string, j is the count of even characters, and k is the count of numericals.
"""

def even_characters(lst):
    """
    Takes a list of strings and returns a summary of the number
    of even characters and the number of digits in each string
    """
    result = []

    for i, string in enumerate(lst):
        even_char = len([char for char in string if char.isdigit() and int(char) % 2 == 0])
        digit_char = len([char for char in string if char.isdigit()])
        
        output = ("The number of even characters in the {}'th input string is {}, and the number of numericals is {}."
                   .format(i+1, even_char, digit_char))
        
        result.append(output)

    return result