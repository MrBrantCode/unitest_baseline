"""
QUESTION:
Develop a function named `shortest_subsequence(input_string)` that takes a string of alphanumeric elements as input and returns the shortest contiguous character sequence containing every single unique alphabetic element present in the string. The function should not consider non-alphabetic elements when determining uniqueness.
"""

def shortest_subsequence(input_string):
    unique_characters = set(char for char in input_string if char.isalpha())

    substr = {}
    start = 0
    temp = {}
    min_length = float('Inf')
    min_str = None

    for i, char in enumerate(input_string):
        if char.isalpha():
            temp[char] = i
            if set(temp.keys()) == unique_characters:
                while start < i:
                    if input_string[start].isalpha() and input_string[start] in temp and temp[input_string[start]] == start:
                        break
                    else:
                        start += 1
                if i - start + 1 < min_length:
                    min_length = i - start + 1
                    min_str = input_string[start:i+1]

    return min_str