"""
QUESTION:
Write a function `peculiar_sum(lst)` that takes a list of strings as input. The strings are either in the format 'YYYY-MM-DD' or consist only of digits. For strings in 'YYYY-MM-DD' format, convert them to 'DD-MM-YYYY' format. For strings consisting only of digits, count the number of odd digits and replace all occurrences of 'i' in the string "the count of odd elements in the string of the input." with the actual count, replacing other instances of 'i' with the count as well. Return the modified list of strings.
"""

def peculiar_sum(lst):
    new_lst = []
    for string in lst:
        if '-' in string:   # it is a 'yyyy-mm-dd' date string
            new_lst.append(string[8:]+'-'+string[5:7]+'-'+string[:4]) 
        else:   # assuming it's a string with digits
            odd_count = sum((int(c) % 2 != 0) for c in string)
            peculiar_string = "the count of odd elements {0}n the str{0}ng {0} of the {0}nput.".format(odd_count)
            new_lst.append(peculiar_string)
    return new_lst