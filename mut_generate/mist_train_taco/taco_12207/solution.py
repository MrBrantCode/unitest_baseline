"""
QUESTION:
You are given four digits N_1, N_2, N_3 and N_4. Determine if these can be arranged into the sequence of digits "1974".

Constraints

* 0 \leq N_1, N_2, N_3, N_4 \leq 9
* N_1, N_2, N_3 and N_4 are integers.

Input

Input is given from Standard Input in the following format:


N_1 N_2 N_3 N_4


Output

If N_1, N_2, N_3 and N_4 can be arranged into the sequence of digits "1974", print `YES`; if they cannot, print `NO`.

Examples

Input

1 7 9 4


Output

YES


Input

1 9 7 4


Output

YES


Input

1 2 9 1


Output

NO


Input

4 9 0 8


Output

NO
"""

def can_form_1974(N1: int, N2: int, N3: int, N4: int) -> str:
    # Convert the digits to a list of strings
    digits = [str(N1), str(N2), str(N3), str(N4)]
    
    # Sort the list of digits
    digits.sort()
    
    # Check if the sorted list matches the sequence "1479"
    if ''.join(digits) == '1479':
        return "YES"
    else:
        return "NO"