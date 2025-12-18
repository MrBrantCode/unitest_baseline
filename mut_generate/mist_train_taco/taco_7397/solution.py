"""
QUESTION:
Write a program which reads a sequence and prints it in the reverse order.

Note

解説

Constraints

* n ≤ 100
* 0 ≤ ai < 1000

Input

The input is given in the following format:


n
a1 a2 . . . an


n is the size of the sequence and ai is the ith element of the sequence.

Output

Print the reversed sequence in a line. Print a single space character between adjacent elements (Note that your program should not put a space character after the last element).

Examples

Input

5
1 2 3 4 5


Output

5 4 3 2 1


Input

8
3 3 4 4 5 8 7 9


Output

9 7 8 5 4 4 3 3
"""

def reverse_sequence(sequence):
    # Reverse the sequence
    reversed_sequence = sequence[::-1]
    # Join the reversed sequence into a string with spaces
    reversed_string = ' '.join(map(str, reversed_sequence))
    return reversed_string