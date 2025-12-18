"""
QUESTION:
Write a function `check_palindrome` that takes two string parameters, `first_text` and `second_text`, and returns a string indicating whether the first text is a palindrome of the second text, considering case-sensitivity and ignoring whitespace.
"""

def entance(first_text, second_text):
    first_text = first_text.replace(" ", "").lower() # removing whitespaces and case-sensitivity
    second_text = second_text.replace(" ", "").lower() # removing whitespaces and case-sensitivity

    if first_text == second_text[::-1]:
        return "The texts are palindromes."
    else:
        return "The texts are not palindromes."