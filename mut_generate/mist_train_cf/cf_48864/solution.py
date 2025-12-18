"""
QUESTION:
Write a function named `reverse_with_hola` that takes an input string, reverses it, and returns a new string comprising "Hola" followed by the reversed input string. The function should work correctly for both single and multiple word strings.
"""

def reverse_with_hola(input_str):
    # slicing that will reverse the string
    reversed_str = input_str[::-1]
    return "Hola " + reversed_str