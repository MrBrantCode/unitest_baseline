"""
QUESTION:
Create a function `repeat_strings` that takes three parameters: a list of strings (`str_list`), a list of numbers (`num_list`), and a target string (`target_str`). The target string will contain one of the strings from `str_list` followed by an index. The function should return a new list where each string in `str_list` is repeated according to its corresponding number in `num_list`, and if the string matches the string portion of `target_str`, it should be repeated according to the number at the index specified by the last character of `target_str`. The function should run in O(n) time complexity.
"""

def repeat_strings(str_list, num_list, target_str):
    # Creating a dictionary where strings are keys and numbers are values
    str_dict = dict(zip(str_list, num_list))

    # Extracting the string and index from the target string
    target_str_data = [char for char in target_str if char.isalpha()]
    target_str_data = "".join(target_str_data)
    target_index = int(target_str[-1])

    # Special repetition for target string
    if target_str_data in str_dict:
        str_dict[target_str_data] = num_list[target_index]

    # Repeat strings
    new_list = [str_dict[str] * str for str in str_list]

    return new_list