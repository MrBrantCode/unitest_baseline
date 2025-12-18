"""
QUESTION:
Write a function `is_sequence_in_list` that checks if a given sequence of strings exists in a nested list. The function should take a nested list and a sequence of strings as input and return True if the sequence exists in the nested list, False otherwise. The function must have a time complexity of O(N), where N is the total number of elements in the nested list.
"""

def is_sequence_in_list(nested_list, sequence):
    """Check if the sequence of strings is in the nested list."""
    def flatten_list(nested_list):
        """Flatten a nested list into a flat list."""
        flat_list = []
        for i in nested_list:
            if type(i) == list:
                flat_list.extend(flatten_list(i))
            else:
                flat_list.append(i)
        return flat_list

    flat_list = flatten_list(nested_list)
    # Join strings to allow checking for sequence
    flat_str = ''.join(map(str, flat_list))
    sequence_str = ''.join(map(str, sequence))
    return sequence_str in flat_str