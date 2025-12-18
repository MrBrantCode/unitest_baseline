"""
QUESTION:
Doraemon gave Nobita a gadget that swaps words inside a string in the following manner :

If there are W words, word 1 is swapped with word W, word 2 is swapped with word W-1 and so on.
The problem is that Nobita himself cannot verify the answer for large strings. Help him write a program to do so.

INPUT : 
the first line of the input contains the number of test cases. Each test case consists of a single line containing the string.

OUTPUT :
output the string with the words swapped as stated above.

CONSTRAINTS :
|string length| ≤ 100000
string contains english alphabets and spaces

SAMPLE INPUT
1
hello world

SAMPLE OUTPUT
world hello
"""

def swap_words_in_string(input_string: str) -> str:
    words = input_string.split()
    n = len(words)
    for i in range(n // 2):
        temp = words[i]
        words[i] = words[n - i - 1]
        words[n - i - 1] = temp
    return ' '.join(words)