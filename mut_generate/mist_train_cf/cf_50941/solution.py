"""
QUESTION:
Create a function named 'add' that takes two numeric parameters and returns their sum. The function should also handle and return any exceptions that occur during the addition operation. Use the function to add two given numbers, 5 and 7, and print the result or any error message that arises.
"""

def add(n1, n2):
    try:
        return n1 + n2
    except Exception as e:
        return str(e)