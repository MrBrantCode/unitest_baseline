"""
QUESTION:
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
 
Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

 
Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.
"""

def is_long_pressed_name(name: str, typed: str) -> bool:
    name_index = 0
    typed_index = 0
    
    while name_index < len(name) and typed_index < len(typed):
        if name[name_index] == typed[typed_index]:
            name_index += 1
            typed_index += 1
        elif typed_index > 0 and typed[typed_index] == typed[typed_index - 1]:
            typed_index += 1
        else:
            return False
    
    # If there are remaining characters in 'typed' that are not long presses of the last character in 'name'
    while typed_index < len(typed):
        if typed[typed_index] != name[-1]:
            return False
        typed_index += 1
    
    # If there are remaining characters in 'name' that were not matched
    return name_index == len(name)