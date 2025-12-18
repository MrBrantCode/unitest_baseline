"""
QUESTION:
You are given a string S of lowercase alphabet characters and the task is to find its matching decimal representation as on the shown keypad. Output the decimal representation corresponding to the string. For ex: if you are given amazon then its corresponding decimal representation will be 262966.
Example 1:
Input:
S = geeksforgeeks
Output: 4335736743357
Explanation:geeksforgeeks is 4335736743357
in decimal when we type it using the given
keypad.
Example 2:
Input:
S = geeksquiz
Output: 433577849
Explanation: geeksquiz is 433577849 in
decimal when we type it using the given
keypad.
Your Task:
Complete printNumber() function that takes string s and its length as parameters and returns the corresponding decimal representation of the given string as a string type. The printing is done by the driver code.
Constraints:
1 ≤ length of String ≤ 100
Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)
"""

def convert_string_to_keypad_digits(input_string: str) -> str:
    # Convert the input string to uppercase to match the dictionary keys
    input_string = input_string.upper()
    
    # Dictionary mapping each character to its corresponding keypad digit
    keypad_mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    
    # Initialize the result string
    result = ''
    
    # Iterate through each character in the input string
    for char in input_string:
        # Append the corresponding digit to the result string
        result += keypad_mapping[char]
    
    return result