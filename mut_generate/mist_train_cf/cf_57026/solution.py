"""
QUESTION:
Write a function `rearrange_string(s)` that takes a string `s` with mixed types of characters (including upper case, lower case letters, numbers, and special characters) and rearranges it so that the first quarter of the string contains only uppercase letters, the second quarter contains only lowercase letters, the third quarter contains only numbers, and the fourth quarter contains only special characters. If a quarter has fewer characters than the others, place the leftover characters in the appropriate order at the end of the string. The length of the string is not fixed and must be considered in the function.
"""

def rearrange_string(s):
    upper, lower, nums, special = [], [], [], []
    
    for char in s:
        if char.isupper():
            upper.append(char)
        elif char.islower():
            lower.append(char)
        elif char.isdigit():
            nums.append(char)
        else:
            special.append(char)
    
    upper_quarter = len(s) // 4
    lower_quarter = upper_quarter * 2
    nums_quarter = upper_quarter * 3

    sorted_s = upper[:upper_quarter] + lower[:upper_quarter] + nums[:upper_quarter] + special[:upper_quarter]
    remainders = upper[upper_quarter:] + lower[upper_quarter:] + nums[upper_quarter:] + special[upper_quarter:]
    sorted_s += remainders

    return ''.join(sorted_s)