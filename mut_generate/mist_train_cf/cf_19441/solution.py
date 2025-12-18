"""
QUESTION:
Write a recursive function `display_lesson` that takes a list of lessons and an integer `n` as input, and returns the nth lesson in the list. The function should not use any built-in list indexing or slicing functions.
"""

def display_lesson(lessons, n):
    """
    Returns the nth lesson in the list using recursion.

    Args:
        lessons (list): A list of lessons.
        n (int): The position of the lesson to be returned.

    Returns:
        str: The nth lesson in the list.
    """
    if n == 0:
        return lessons[0]
    else:
        return display_lesson(lessons[1:], n-1)