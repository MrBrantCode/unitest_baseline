"""
QUESTION:
Solve The Mystery

Input:
First line contains T - number of test cases.
Following T lines each contains a string of characters in the range [a-z] only  

Output:
Print a numeric string for each test case.  

Constraints:
1 ≤ T ≤ 100
1 ≤ Length of String ≤ 100  

SAMPLE INPUT
10
key
to
control
nine
tails
is
in
your
hand
phone

SAMPLE OUTPUT
539
86
2668765
6463
82457
47
46
9687
4263
74663
"""

def convert_string_to_numeric(input_string: str) -> str:
    numeric_string = ''
    for char in input_string:
        if char in 'abc':
            numeric_string += '2'
        elif char in 'def':
            numeric_string += '3'
        elif char in 'ghi':
            numeric_string += '4'
        elif char in 'jkl':
            numeric_string += '5'
        elif char in 'mno':
            numeric_string += '6'
        elif char in 'pqrs':
            numeric_string += '7'
        elif char in 'tuv':
            numeric_string += '8'
        elif char in 'wxyz':
            numeric_string += '9'
    return numeric_string