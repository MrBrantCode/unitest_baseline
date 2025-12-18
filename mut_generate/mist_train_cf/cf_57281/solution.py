"""
QUESTION:
Create a function named 'booleanSum' that takes a list of boolean values (True/False) and integer values as a parameter. The function should iterate over the list and maintain three counters: 'true_sum', 'false_sum', and 'integer_sum'. For every boolean value encountered, increment 'true_sum' for True and 'false_sum' for False. For every integer encountered, add its value to 'integer_sum'. The function should return the values of 'true_sum' and 'false_sum'.
"""

def booleanSum(arr):
    true_sum = 0
    false_sum = 0
    integer_sum = 0
    for item in arr:
        if type(item) == bool:
            if item == True:
                true_sum += 1
            elif item == False:
                false_sum += 1
        elif type(item) == int:
            integer_sum += item
    return true_sum, false_sum