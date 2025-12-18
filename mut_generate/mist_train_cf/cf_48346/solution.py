"""
QUESTION:
Write a function `string_duplicate` that takes a string and an integer as input. The function should return a string where each word from the input string is repeated a number of times equal to the input integer, while maintaining the original word order.
"""

def string_duplicate(user_string, user_num):
    # we split the string into separate words
    split_string = user_string.split(" ")
    new_string = []

    # we iterate through each word in the string
    for word in split_string:
        # we duplicate the word according to the number entered
        new_string.append(word * user_num)
    
    # return the new string joined with a space
    return " ".join(new_string)