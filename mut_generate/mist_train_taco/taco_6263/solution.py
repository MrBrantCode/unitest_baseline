"""
QUESTION:
A number is self-descriptive when the n'th digit describes the amount n appears in the number.

E.g. 21200:

There are two 0's in the number, so the first digit is 2.

There is one 1 in the number, so the second digit is 1.

There are two 2's in the number, so the third digit is 2.

There are no 3's in the number, so the fourth digit is 0.

There are no 4's in the number, so the fifth digit is 0


Numbers can be of any length up to 9 digits and are only full integers. For a given number derive a function ```selfDescriptive(num)``` that returns; ```true``` if the number is self-descriptive or ```false``` if the number is not.
"""

from collections import Counter

def is_self_descriptive(num):
    # Convert the number to a list of its digits
    s = [int(a) for a in str(num)]
    
    # Count the occurrences of each digit
    cnt = Counter(s)
    
    # Check if each digit correctly describes the count of its index
    return all((cnt[i] == b for (i, b) in enumerate(s)))