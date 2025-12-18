"""
ORIGINAL QUESTION:
Create a function named `check_palindrome` that takes a string `s` as input, removes spaces, and converts it to lowercase. It should then check if `s` is a palindrome and count the occurrence of each character. If `s` is a palindrome, the function should return whether all characters occur an even number of times or not. If `s` is not a palindrome, the function should return a message indicating so. The function's output should include the character count dictionary. The function should not take any additional inputs other than the string `s`.
"""

def entrance(s):
    s = s.replace(" ", "")  # remove spaces
    s = s.lower()  # convert string to lowercase
    reversed_s = s[::-1]  # reverse the string
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    if s == reversed_s:
        if all(value % 2 == 0 for value in char_count.values()):
            return "The string is a palindrome and all characters occur even times: " + str(char_count)
        else:
            return "The string is a palindrome but not all characters occur even times: " + str(char_count)
    else:
        return "The string is not a palindrome: " + str(char_count)