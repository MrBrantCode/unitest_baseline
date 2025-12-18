"""
QUESTION:
The EEE classes are so boring that the students play games rather than paying attention during the lectures. Harsha and Dubey are playing one such game.

The game involves counting the number of anagramic pairs of a given string (you can read about anagrams from here). Right now Harsha is winning. Write a program to help Dubey count this number quickly and win the game!

-----Input-----
The first line has an integer T which is the number of strings. Next T lines each contain a strings. Each string consists of lowercase english alphabets only.

-----Output-----
For each string, print the answer in a newline.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 1 ≤ length of each string ≤ 100

-----Example-----
Input:
3
rama
abba
abcd
Output:
2
4
0

-----Explanation-----
rama has the following substrings:

- r
- ra
- ram
- rama
- a
- am
- ama
- m
- ma
- a
Out of these, {5,10} and {6,9} are anagramic pairs.

Hence the answer is 2.

Similarly for other strings as well.
"""

def count_anagramic_pairs(strings):
    """
    Counts the number of anagramic pairs for each string in the input list.

    Parameters:
    strings (list of str): A list of strings where each string consists of lowercase English alphabets.

    Returns:
    list of int: A list of integers where each integer corresponds to the number of anagramic pairs for the respective string in the input list.
    """
    
    def sort_str(s):
        o = []
        for c in s:
            o.append(c)
        o.sort()
        return ''.join(o)

    def find_ana(s):
        if len(s) <= 1:
            return 0
        h = {}
        c = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                t = sort_str(s[i:j])
                if t in h:
                    c += h[t]
                    h[t] += 1
                else:
                    h[t] = 1
        return c

    results = []
    for s in strings:
        results.append(find_ana(s))
    
    return results