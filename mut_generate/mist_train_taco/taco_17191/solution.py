"""
QUESTION:
problem

Create a program that counts the number of consecutive JOI or IOI characters in a given character string. The character string consists only of uppercase letters of the alphabet. For example, the character string "JOIOIOI" in the figure below contains JOI in one place and IOI in two places.

<image>



input

The input consists of multiple datasets. Each dataset is one line and consists of uppercase letters of the alphabet of 10,000 characters or less. Input ends with EOF.

The number of datasets does not exceed 5.

output

For each dataset, output the number of JOIs found in the first line and the number of IOIs found in the second line.

Examples

Input

JOIJOI
JOIOIOIOI
JOIOIJOINXNXJIOIOIOJ


Output

2
0
1
3
2
3


Input

None


Output

None
"""

def count_joi_ioi(input_string: str) -> tuple[int, int]:
    """
    Counts the number of consecutive "JOI" and "IOI" substrings in the given input string.

    Parameters:
    input_string (str): A string consisting of uppercase letters of the alphabet.

    Returns:
    tuple[int, int]: A tuple where the first element is the count of "JOI" substrings
                     and the second element is the count of "IOI" substrings.
    """
    joi_count = 0
    ioi_count = 0
    
    for i in range(len(input_string) - 2):
        substring = input_string[i:i + 3]
        if substring == 'JOI':
            joi_count += 1
        elif substring == 'IOI':
            ioi_count += 1
    
    return joi_count, ioi_count