"""
QUESTION:
Write a recursive function called `display_lesson` that takes a list of lessons and a lesson number `n` as input, and returns the nth lesson from the list without using any built-in list indexing or slicing functions.
"""

def display_lesson(lessons, n):
    if n == 1:
        return lessons[0]
    else:
        return display_lesson(lessons[1:], n - 1)