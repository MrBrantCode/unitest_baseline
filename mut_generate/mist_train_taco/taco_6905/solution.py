"""
QUESTION:
James came across the next problem in a newspaper. It said 

“Bring order to the word and your nation shall be bestowed upon with the same”

The task was to print the letters of the word in the order of their occurrence in the alphabet.

Take a string input(all alphabets and in lower case) from the user and print the character in alphabetical order.

Sample Input:
elementary

Sample Output:
aeeelmntry

SAMPLE INPUT
elementary

SAMPLE OUTPUT
aeeelmntry
"""

def sort_characters_alphabetically(input_string: str) -> str:
    """
    Sorts the characters of the input string in alphabetical order.

    Parameters:
    input_string (str): A string containing only lowercase alphabets.

    Returns:
    str: A string where the characters of the input string are sorted in alphabetical order.
    """
    # Initialize a list to count occurrences of each character
    lst = [0] * 26
    
    # ASCII value of 'a'
    asc = ord('a')
    
    # Count the occurrences of each character in the input string
    for char in input_string:
        lst[ord(char) - asc] += 1
    
    # Build the sorted string
    sorted_string = ''
    for i in range(26):
        sorted_string += chr(i + asc) * lst[i]
    
    return sorted_string