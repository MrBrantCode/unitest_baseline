"""
QUESTION:
Write a function `remove_max_num` that takes a string of comma-separated numerical values as input, removes the highest number, and returns a new string containing the remaining values, retaining the comma delimiters. The input string contains at least one numerical value, and the numerical values are separated by a comma and a space.
"""

def remove_max_num(str_nums):
    # Split the string into a list of strings
    list_nums = str_nums.split(", ")

    # Convert each string in the list to an integer
    list_nums = [int(num) for num in list_nums]

    # Find the maximum number in the list
    max_num = max(list_nums)

    # Remove the maximum number from the list
    list_nums.remove(max_num)

    # Convert the list of integers back into a list of strings
    list_nums = [str(num) for num in list_nums]

    # Join the list of strings into a single string with comma delimiters
    str_nums = ", ".join(list_nums)

    return str_nums