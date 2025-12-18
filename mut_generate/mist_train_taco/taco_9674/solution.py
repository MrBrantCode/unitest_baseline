"""
QUESTION:
Given a sentence in the form of a string in uppercase, convert it into its equivalent mobile numeric keypad sequence. Please note there might be spaces in between the words in a sentence and we can print spaces by pressing 0.
 
Example 1:
Input:
S = "GFG"
Output: 43334
Explanation: For 'G' press '4' one time.
For 'F' press '3' three times.
Example 2:
Input:
S = "HEY U"
Output: 4433999088
Explanation: For 'H' press '4' two times.
For 'E' press '3' two times. For 'Y' press '9' 
three times. For white space press '0' one time.
For 'U' press '8' two times.
 
Your Task:  
You dont need to read input or print anything. Complete the function printSequence() which takes a string as input parameter and returns its equivalent mobile numeric keypad sequence as a string.
 
Expected Time Complexity: O(Length of String)
Expected Auxiliary Space: O(Length of String)
 
Constraints:
1 <= Length of String <= 10^{5}
Characters of string can be empty space or capital alphabets.
"""

def convert_to_keypad_sequence(sentence: str) -> str:
    # Mapping of each character to its corresponding keypad sequence
    keypad_map = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
        ' ': '0'
    }
    
    # Initialize the result sequence
    sequence = ''
    
    # Convert each character in the sentence to its corresponding keypad sequence
    for char in sentence:
        sequence += keypad_map[char]
    
    return sequence