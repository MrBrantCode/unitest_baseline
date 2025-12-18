"""
QUESTION:
Develop a function `convert_num_string_to_num` that takes an English language alpha-numeric expression as a string input and returns its corresponding numerical representation as an integer. The input string may contain the words for numbers 0-19, tens, hundreds, thousands, millions, and billions. It may also contain the word "and" as a separator. The function should correctly handle expressions with multiple parts (e.g., "one thousand two hundred and thirty four").
"""

# mapping of numeric string to their numerical values
num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0,
            "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
            "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
            "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
            "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
            "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000,
            "million": 1000000, "billion": 1000000000, "and": ""}


def convert_num_string_to_num(num_string):
    # split the string into list
    num_string = num_string.split()
    total = 0
    temp_num = 0
    for word in num_string:
        if word != "and":
            num = num_dict[word]
            # if num is 100 or 1000 or 1000000, multiply it with last number
            if num >= 100:
                temp_num *= num
                # add temporary number to total
                if temp_num >= 1000:
                    total += temp_num
                    temp_num = 0
            else:
                temp_num += num
        else:
            continue
    total += temp_num
    return total