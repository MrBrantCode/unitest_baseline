"""
QUESTION:
Create a function called `ascii_quartet` that takes two string inputs `str1` and `str2`. The function should return a string containing the ASCII values of the last four characters from each input string, separated by spaces. If a string has less than four characters, include all its characters. The function should not include any trailing spaces in the output.
"""

def ascii_quartet(str1, str2):
    quartet1 = str1[-4:]
    quartet2 = str2[-4:]
    
    ascii_str = ""
    for char in quartet1 + quartet2:
      ascii_str += str(ord(char)) + " "

    return ascii_str.rstrip()