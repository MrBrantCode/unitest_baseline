"""
QUESTION:
Implement the function `solve(Map_B)` that takes a dictionary `Map_B` as input, removes the key-value pairs with values less than 10, and returns a new dictionary where the keys are the remaining original keys concatenated with their respective remaining values in string form. The value in the new dictionary should be 'Short' if the word representation of the value has less than or equal to 5 letters, and 'Long' otherwise. Use a helper method to convert integers to words without using any additional libraries.
"""

def convert_to_words(num):
    """Converts numbers to words."""
    if num==1:
        return 'one'
    if num==2:
        return 'two'
    if num==3:
        return 'three'
    if num==4:
        return 'four'
    if num==5:
        return 'five'
    if num==6:
        return 'six'
    if num==7:
        return 'seven'
    if num==8:
        return 'eight'
    if num==9:
        return 'nine'
    if num==10:
        return 'ten'
    if num==20:
        return 'twenty'
    if num>20:
        return 'long number'

def entance(Map_B):
    """Removes the key-value pairs with values less than 10 and returns a new dictionary 
    where the keys are the remaining original keys concatenated with their respective 
    remaining values in string form. The value in the new dictionary should be 'Short' 
    if the word representation of the value has less than or equal to 5 letters, and 'Long' otherwise."""
    result_map = {}
    
    for key, value in Map_B.items():
        if value < 10:
            continue
        new_key = key + str(value)
        new_value = convert_to_words(value)
        if len(new_value) <= 5:
            result_map[new_key] = 'Short'
        else:
            result_map[new_key] = 'Long'
    
    return result_map