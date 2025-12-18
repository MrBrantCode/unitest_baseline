"""
QUESTION:
Write a function `update_sequence(sequence)` that takes a string of comma-separated numerical values. Extract the highest and smallest number from the sequence, multiply these two numbers, and return a new string containing the remaining values, retaining the comma delimiters. Ensure the function handles edge cases, such as empty strings or strings with only one value. The function should return a tuple containing the new string and the product of the smallest and largest numbers.
"""

def update_sequence(sequence):
    if not sequence:   
        return ("", float('-inf')) 

    values = list(map(int, [value.strip() for value in sequence.split(',')]))

    if len(values) == 1:  
        return ("", values[0]) 
  
    min_value = min(values)
    max_value = max(values)

    values.remove(min_value)
    values.remove(max_value)
    remaining_sequence = ', '.join(map(str, values))

    return (remaining_sequence, min_value * max_value)