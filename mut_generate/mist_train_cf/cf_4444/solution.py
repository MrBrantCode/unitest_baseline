"""
QUESTION:
Create a function named `reverse_string` that takes a single string argument and prints the reversed string. The function should not use any built-in string reversal functions or libraries, and instead use basic string manipulation methods. The input string can contain special characters and spaces, and its length should not exceed 1000 characters.
"""

def reverse_string(string):
    if len(string) > 1000:
        print("Error: String length exceeds the maximum limit (1000 characters).")
        return
    
    reversed_string = ""
    
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    
    print(reversed_string)