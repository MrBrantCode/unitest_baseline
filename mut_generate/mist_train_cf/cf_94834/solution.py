"""
QUESTION:
Create a program with the following functions:

- `get_name(names)`: This function takes a list of names as input, prints them in sorted order, and returns the sorted list.

- `count_names_starting_with(names, letter)`: This function takes a list of names and a letter as input and returns the count of names that start with the given letter.

- `is_name_present(names, name)`: This function takes a list of names and a name as input and returns `True` if the name is present in the list, `False` otherwise.

All names should be treated as case-sensitive.
"""

def entrance(names):
    def get_name(names):
        sorted_names = sorted(names)
        print("Here are the names:")
        for name in sorted_names:
            print(name)
        return sorted_names

    def count_names_starting_with(names, letter):
        count = 0
        for name in names:
            if name.startswith(letter):
                count += 1
        return count

    def is_name_present(names, name):
        return name in names

    return get_name, count_names_starting_with, is_name_present