"""
QUESTION:
Your task is very simple. Given an input string s, case\_sensitive(s), check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

For example, case\_sensitive('codewars') returns [True, []], but case\_sensitive('codeWaRs') returns [False, ['W', 'R']].


Goodluck :)

Have a look at my other katas!

Alphabetically ordered 
Find Nearest square number 
Not prime numbers
"""

def check_lowercase_and_non_lowercase_chars(s: str) -> tuple[bool, list[str]]:
    """
    Checks whether all characters in the input string are lowercase.
    Returns a tuple containing a boolean indicating if all characters are lowercase
    and a list of characters that are not lowercase, in the order of their appearance.

    :param s: The input string to be checked.
    :return: A tuple (is_all_lowercase, non_lowercase_chars)
    """
    is_all_lowercase = s.islower()
    non_lowercase_chars = [c for c in s if c.isupper()]
    return is_all_lowercase, non_lowercase_chars