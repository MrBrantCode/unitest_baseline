"""
QUESTION:
Create a function named `generate_dictionary` that takes two parameters, `list_a` and `list_b`, and returns a dictionary. The function should work under the following conditions:
- `list_a` contains unique elements.
- `list_b` contains strings.
- The length of `list_a` is equal to the length of `list_b`.
- The function should sort `list_a` in ascending order and `list_b` in descending order.
- It should then create a dictionary where each key-value pair consists of a corresponding element from `list_a` as the key and from `list_b` as the value.
"""

def generate_dictionary(list_a, list_b):
    # Sort list_a in ascending order and list_b in descending order
    list_a.sort()
    list_b.sort(reverse=True)

    # Create a dictionary using dictionary comprehension
    return {a: b for a, b in zip(list_a, list_b)}