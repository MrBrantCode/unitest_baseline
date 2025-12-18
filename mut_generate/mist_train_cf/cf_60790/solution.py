"""
QUESTION:
Create a function `frequency(arr)` that constructs a numerical distribution table representing the frequency of each element within a given mixed list of integers and strings. For strings, each character should be treated individually, and their frequency should be calculated separately. The function should return a dictionary where the keys are the elements (either integers or characters) and the values are their corresponding frequencies. The function should be able to handle a list containing both integers and strings.
"""

def frequency(arr):
    table = {}
    for i in arr:
        if isinstance(i, str):
            for char in i:
                if char in table:
                    table[char] += 1
                else:
                    table[char] = 1
        else:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
    return table