"""
QUESTION:
Create a custom iterator class `LabelIterator` and a function `count_strings_with_label`. The `LabelIterator` class takes a list of strings and a label as input and iterates over the list, returning only the strings with the specified label. The `count_strings_with_label` function takes a list of strings and a label as input and returns the count of strings with that label. 

The `LabelIterator` class should have the `__iter__` and `__next__` methods to make it an iterator. The `__next__` method should raise a `StopIteration` exception when there are no more strings with the specified label. The `count_strings_with_label` function should return 0 if the label is not found in the list of strings. The function should assume that a string has the specified label if the string starts with the label.
"""

def count_strings_with_label(strings, label):
    return sum(1 for string in strings if string.startswith(label))