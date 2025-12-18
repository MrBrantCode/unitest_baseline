"""
QUESTION:
Create a function named `sort_by_middle_letter` that takes a list of words as input. The function should return a list of words that have an odd number of letters and a length of at least 5, sorted in ascending order by their middle letter.
"""

def sort_by_middle_letter(words):
    return sorted([word for word in words if len(word) % 2 == 1 and len(word) >= 5], key=lambda x: x[len(x)//2])