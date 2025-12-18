"""
QUESTION:
Write a function named `extract_third_last` that takes a tuple `colors` as input and returns the third last item from the tuple. If the tuple has less than three items, it should print a meaningful error message instead of crashing.
"""

def extract_third_last(colors):
    try:
        return colors[-3]
    except IndexError:
        print("Tuple is too small to have a third last item")