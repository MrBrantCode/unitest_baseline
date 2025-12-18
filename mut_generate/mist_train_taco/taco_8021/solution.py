"""
QUESTION:
Andi and Bob were friends since childhood days. But, as they grew up Bob started behaving weird and this used to irritate Andi. Once, while Andi took a break after typing a large program Bob came from nowhere and swapped some alphabet keys on Andi's keyboard.

Andi got very angry on seeing this and decided to end their friendship once forever. As we all know Bob is very good at heart and never does anything wrong intentionally. He decided to type the remaining program with the same keyboard Configuration.
Given the original fragment of the code that Bob needs to type, You need to tell Bob the code that he should type to get the original code as output.

Help him saving his friendship with Andi.

INPUT  :

First line of the input contains a single integer N denoting the number of swaps done by Bob. Next N lines contain a pair of characters A,B denoting the characters which are swapped by Bob (Note that Bob performs these swaps in the given order).
From the very next line of input the remaining fragment of the code starts and ends with an end of file character.

OUTPUT:

print the fragment of the program that Bob types.

CONSTRAINTS:

1 ≤ N ≤ 10^6

1 ≤ |length of codefragment| ≤ 10^6

code fragment contains uppercase and lowercase english alphabets only and space.

A,B belongs to Alphabet set (both upper case and lower case letters are included).

SAMPLE INPUT
1
W H
WelloHorld

SAMPLE OUTPUT
HelloWorld

Explanation

For the given test case:

Letter W is swapped with the letter H. So, to type WelloHorld Bob must type HelloWorld on Andi's keyboard.
"""

import string

def restore_code_fragment(n, swaps, code_fragment):
    # Initialize the dictionary with default mappings
    d = {}
    for x in string.ascii_uppercase:
        d[x] = x
    
    # Perform the swaps
    for a, b in swaps:
        a, b = a.upper(), b.upper()
        d[a], d[b] = d[b], d[a]
    
    # Extend the dictionary to include lowercase mappings
    for x in string.ascii_lowercase:
        d[x] = d[x.upper()].lower()
    
    # Create a reverse mapping dictionary
    m = {}
    for k, v in list(d.items()):
        m[v] = k
    
    # Restore the code fragment using the reverse mapping
    restored_fragment = ''.join([m[c] if c in m else c for c in code_fragment])
    
    return restored_fragment