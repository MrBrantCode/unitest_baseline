"""
QUESTION:
Write a function `last_instance_in_string(main_string, substring)` that returns the substring and the rest of the main string, starting from the last occurrence of the substring in the main string. If the substring is not found, return 'Substring not found in the main string.'
"""

def last_instance_in_string(main_string, substring):
    position = main_string.rfind(substring)
    if position != -1:
        return main_string[position:]
    else:
        return 'Substring not found in the main string.'