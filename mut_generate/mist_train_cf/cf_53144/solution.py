"""
QUESTION:
Create a function `sorted_unique_absolute_values` that takes a sequence of integers as input. The function should return a list of their absolute values arranged in ascending order, with no duplicates. If the input is not a list, the function should return "Please provide a list." The function should not use built-in functions for sorting or removing duplicates. The input sequence may contain both positive and negative integers.
"""

def sorted_unique_absolute_values(sequence):
    """Return sorted list of unique absolute values by handling incorrect inputs and without using in-built functions"""

    if not isinstance(sequence, list):
        return "Please provide a list."

    output = []
    for number in sequence:
        if not isinstance(number, int):
            continue    # skip non-integers
        abs_number = number if number >= 0 else -number

        if len(output) == 0 or abs_number > output[-1]:
            output.append(abs_number)

        else:
            for i in range(len(output)):
                if abs_number == output[i]:
                    break   # the number is already in the list
                elif abs_number < output[i]:
                    output = output[:i] + [abs_number] + output[i:]
                    break
                
    return output