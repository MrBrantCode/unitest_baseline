"""
QUESTION:
Write a function named `count_apples` that takes a list of fruits as input and returns the total count of 'apple' in the list, regardless of case sensitivity. The function should not use a for-loop and should be as concise as possible.
"""

def count_apples(fruit_basket):
    return [fruit.lower() for fruit in fruit_basket].count('apple')