"""
QUESTION:
Write a function `find_max_min` that takes a string of four integer values separated by commas as input, and returns the maximum and minimum values from the list as integers. The input string may contain spaces after the commas, and the function should handle potential exceptions that might occur during execution.
"""

def find_max_min(nums: str):
    try:
        nums_list = nums.replace(" ", "").split(",")
        int_list = [int(num) for num in nums_list]
        max_num = max(int_list)
        min_num = min(int_list)
    except ValueError:
        return "Error: Ensure all items are valid integers"
    except Exception as e:
        return str(e)
    return max_num, min_num