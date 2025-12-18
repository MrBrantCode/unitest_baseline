"""
QUESTION:
Create a function named `reverse_string` that takes a string as input and prints out its reverse. The function should not use any built-in functions or libraries that directly reverse strings. It should use basic string manipulation methods to handle cases where the input string contains special characters and spaces. The function should be able to handle strings with a maximum length of 1000 characters.
"""

def reverse_string(string):
    # Check if string length is within the limit
    if len(string) > 1000:
        print("Error: String length exceeds the maximum limit (1000 characters).")
        return
    
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    
    # Iterate over the characters in the string in reverse order
    for i in range(len(string)-1, -1, -1):
        # Append each character to the reversed_string variable
        reversed_string += string[i]
    
    # Print the reversed string
    print(reversed_string)