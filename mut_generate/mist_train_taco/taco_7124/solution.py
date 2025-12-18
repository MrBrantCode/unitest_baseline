"""
QUESTION:
Iroha loves Haiku. Haiku is a short form of Japanese poetry. A Haiku consists of three phrases with 5, 7 and 5 syllables, in this order.
To create a Haiku, Iroha has come up with three different phrases. These phrases have A, B and C syllables, respectively. Determine whether she can construct a Haiku by using each of the phrases once, in some order.

-----Constraints-----
 - 1≦A,B,C≦10

-----Input-----
The input is given from Standard Input in the following format:
A B C

-----Output-----
If it is possible to construct a Haiku by using each of the phrases once, print YES (case-sensitive). Otherwise, print NO.

-----Sample Input-----
5 5 7

-----Sample Output-----
YES

Using three phrases of length 5, 5 and 7, it is possible to construct a Haiku.
"""

def can_form_haiku(A: int, B: int, C: int) -> str:
    # Create a list of the syllable counts
    syllables = [A, B, C]
    # Sort the list to check if it matches the Haiku pattern
    syllables.sort()
    # Check if the sorted list matches the Haiku pattern [5, 5, 7]
    if syllables == [5, 5, 7]:
        return "YES"
    else:
        return "NO"