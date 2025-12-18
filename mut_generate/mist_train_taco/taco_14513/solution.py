"""
QUESTION:
We, the researchers who discovered and investigated the ancient nation Iwashiro, finally discovered the temple in the center of Iwashiro. A lithograph dedicated to the god of Iwashiro was stored in the temple. On the lithograph, two strings were written, one for each sentence and one for the spell.

In Iwashiro, how many times a spell appears in a sentence has an important meaning. However, it is considered that all the characters contained in the spell appear in order, and some of them appear in the sentence in a discrete manner once. For example, if the sentence is "abab" and the spell is "ab", then "ab" appears three times in "abab", including non-continuous ones (three ways: abab, abab, and abab).

Create a program that prints how many times a spell appears in a sentence when it is given a sentence and a spell.



Input

The input is given in the following format.


t
b b


The first line is given the string t that represents the text written on the lithograph. The second line is given the string b that represents the spell written on the lithograph. Both strings are composed of only lowercase letters and have a length of 1 or more and 1000 or less.

Output

Prints how many times a spell appears in a sentence on one line. However, the value to be output can be very large, so instead output the remainder divided by 1,000,000,007.

Examples

Input

abab
ab


Output

3


Input

aaaabaaaabaaaabaaaab
aaaaa


Output

4368


Input

data
structure


Output

0
"""

def count_spell_in_sentence(sentence: str, spell: str) -> int:
    MOD = 10**9 + 7
    cnts = [0] * (len(spell) + 1)
    cnts[0] = 1
    
    for c in sentence:
        for i in range(len(spell) - 1, -1, -1):
            if c == spell[i]:
                cnts[i + 1] = (cnts[i + 1] + cnts[i]) % MOD
    
    return cnts[-1]