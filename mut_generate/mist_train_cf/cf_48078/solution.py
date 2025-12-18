"""
QUESTION:
Implement a function `convert_string_to_int` that takes an alphanumeric string as input and returns an integer. The string may contain non-numeric characters, which should be ignored. The function should also handle negative and positive signs, considering the cumulative effect of consecutive signs (two '-' symbols in sequence are treated as '+', and '-' and '+' symbols in sequence are treated as '-').
"""

def convert_string_to_int(input_string):
    # keep track of signs
    is_negative = False
    total = 0
    input_string_list = list(input_string)
    while len(input_string_list)>0:
        val = input_string_list.pop(0)
        
        # if it's a digit, add it to the total
        if val.isdigit():
            total = total*10 + int(val)
            continue
        
        # if it's a sign, update the is_negative flag accordingly
        if val == '-':
            is_negative = not is_negative
        elif val == '+':
            continue
        else:
            continue
            
    return total if not is_negative else -total