"""
QUESTION:
Given a word consisting of lowercase English letters, write a program to remove duplicates from the word. The characters in the output must preserve the same order, as their first appearance in the original word.

Input Format

The input consists of several test cases.
The first line of the input file contains a positive integer T, the number of test cases.
Then, T lines follow, each containing a single word W (no spaces, only lowercase English letters).

Output Format

The output must contain exactly T lines, each line containing a single word, the required answer.

Constraints

1 ≤ T ≤ 100
1 ≤ |W| ≤ 31

SAMPLE INPUT
2
hello
world
mississippi

SAMPLE OUTPUT
helo
world
misp
"""

def remove_duplicates_from_word(word: str) -> str:
    index = [0] * 26  # Initialize an array to keep track of character occurrences
    new_word = ""
    
    for char in word:
        asc_val = ord(char) - 97  # Calculate the ASCII value of the character
        if index[asc_val] == 0:  # If the character has not been encountered before
            new_word += char
            index[asc_val] = 1  # Mark the character as encountered
    
    return new_word