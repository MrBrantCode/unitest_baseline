"""
QUESTION:
Write a function `apple_count(fruit_basket)` that takes a list of fruits as input and returns the number of 'apple' present in the list. The function should be optimized for time complexity and memory usage. Implement unit test cases to cover various scenarios, including an empty basket, a basket with only apples, and a basket with multiple types of fruits.
"""

def apple_count(fruit_basket):
    return fruit_basket.count('apple')