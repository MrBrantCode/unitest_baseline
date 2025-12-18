"""
QUESTION:
After the Tatvik Hiring Challenge, Karan's NLP professor has given him another homework. Since Manhattan Associates Hiring Challenge is round the corner and Karan is busy preparing for it, he turns to you for help.

Given a string, replace all the consecutively occurring characters by a single, same character.

Input:

The first line contains the number of test cases T. Each test case contains the string, on a separate line.

Output:

Print the modified string, each on a new line.

Constraints:

1 ≤ T ≤ 100

1 ≤ length(string) < 10^6

SAMPLE INPUT
1
aabbcc

SAMPLE OUTPUT
abc
"""

def remove_consecutive_duplicates(input_string: str) -> str:
    if not input_string:
        return input_string
    
    output_string = input_string[0]  # Start with the first character
    
    for char in input_string[1:]:
        if char != output_string[-1]:
            output_string += char
    
    return output_string