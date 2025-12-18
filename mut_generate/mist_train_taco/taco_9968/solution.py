"""
QUESTION:
As a New Year's gift, Dolphin received a string s of length 19.

The string s has the following format: [five lowercase English letters],[seven lowercase English letters],[five lowercase English letters].

Dolphin wants to convert the comma-separated string s into a space-separated string.

Write a program to perform the conversion for him.  

-----Constraints-----
 - The length of s is 19.
 - The sixth and fourteenth characters in s are ,.
 - The other characters in s are lowercase English letters.

-----Input-----
The input is given from Standard Input in the following format:
s

-----Output-----
Print the string after the conversion.

-----Sample Input-----
happy,newyear,enjoy

-----Sample Output-----
happy newyear enjoy

Replace all the commas in happy,newyear,enjoy with spaces to obtain happy newyear enjoy.
"""

def convert_comma_separated_to_space_separated(s: str) -> str:
    """
    Converts a comma-separated string of length 19 into a space-separated string.

    Parameters:
    s (str): A string of length 19, formatted as [five lowercase English letters],[seven lowercase English letters],[five lowercase English letters].

    Returns:
    str: A string where all commas in the input string are replaced with spaces.
    """
    return ' '.join(s.split(','))