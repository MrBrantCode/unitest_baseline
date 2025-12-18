"""
QUESTION:
Create a function `split_numbers` that takes a string as input, extracts and returns all the numbers in the string as a list of strings. If no numbers are found in the string, return a list containing the sum of the ASCII values of all vowels in the string as a string. If the input string is empty, return a list containing the string "0".
"""

def split_numbers(s):
    # empty string condition
    if not s:
        return ["0"]
    
    # to store the numbers
    nums = []

    # string to store numbers temporarily
    str_num = ""

    # iterate over all characters in string
    for char in s:
        # if character is digit
        if char.isdigit():
            str_num += char
        else:  # if not a digit
            if str_num:
                nums.append(str_num)
                str_num = ""

    # push last number in string to vector
    if str_num:
        nums.append(str_num)

    # if no numbers were found
    if not nums:
        sum_ascii = 0
        for char in s:
            if char.lower() in 'aeiou':
                # add ASCII value to sum
                sum_ascii += ord(char)
        nums.append(str(sum_ascii))

    return nums