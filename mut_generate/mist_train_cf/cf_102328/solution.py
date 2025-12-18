"""
QUESTION:
Create a method named `build_even_dictionary` that takes a list as input and returns a dictionary. The input list may contain integers, floats, and strings, including duplicates and negative numbers. The dictionary should include only unique even numbers greater than 5, with the even number as both the key and the value.
"""

def build_even_dictionary(lst):
    even_dict = {}
    for num in lst:
        if isinstance(num, (int, float)) and num % 2 == 0 and num > 5:
            even_dict[num] = num
    return even_dict