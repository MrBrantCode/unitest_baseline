"""
QUESTION:
Write a function `by_length` that takes an array of integers as input. The function should sort the integers ranging from 1 to 9 in ascending order, reverse the sorted array, and then substitute each digit with its corresponding word from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine". Ignore any integers outside this range. Return the resulting array of words.
"""

def by_length(arr):
    words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    one_to_nine = [x for x in arr if 1 <= x <= 9]
    one_to_nine.sort(reverse=True)
    return [words[num - 1] for num in one_to_nine]