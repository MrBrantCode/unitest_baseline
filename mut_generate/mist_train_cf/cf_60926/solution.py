"""
QUESTION:
Write a function named `inverse` that prints a given string in reverse order without using any pre-existing string reversal functions or iterative constructs like loops. The function should take a string and an optional index parameter.
"""

def inverse(s, i=0):
    if i == len(s):
        return
    else:
        inverse(s, i+1)
        print(s[i], end='')