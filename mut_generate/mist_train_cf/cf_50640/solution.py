"""
QUESTION:
Design a Python function called 'vowels_consonants' that takes an input string and segregates each individual character into either vowels or consonants. The function should accommodate strings with Unicode alphabetic characters and handle edge cases including strings composed entirely of non-alphabetic characters, strings that only contain vowels or consonants, and empty strings.
"""

def vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    dicv = {i: s.count(i) for i in set(s) if i in vowels}
    dicc = {i: s.count(i) for i in set(s) if i in consonants}
    return dicv, dicc