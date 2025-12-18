"""
QUESTION:
Monkeys in the army were fascinated by a game which people of Lanka used to play. It consist of forming Anagrams of a string of letters. An anagram is a string formed by rearranging the letters of a given string. For example one of the anagram of "elvis" is "lives".

You will be provided with two string 's' and 't'. You can insert letters in string 's' so that string 't' is one of the Anagram of the newly formed string (after insertion in 's').

Your job is to count the number of unique letter insertions made if possible otherwise print -1. For example if 'a' is inserted thrice then it will counted as 1.
String will only consist of lower case letters ('a' - 'z').

Input:

First line will contain T ,denoting the number of test cases.
Each test case  will consist of two lines. First line will contain string s and next line will contain string t.

Ouput:

Output the required answer in new line.

Constraint:

0  <  T  < =20

0 < |s| ≤ 1000

0 < |t| ≤ 1000

|s| ≤ |t|

where, |s| denotes the length of the string s.

Note: You can insert letter(s) anywhere in the string 's'.

SAMPLE INPUT
2
a
agh

ankur
durgesh

SAMPLE OUTPUT
2
-1
"""

def count_unique_insertions(s: str, t: str) -> int:
    s_list = list(s)
    t_list = list(t)
    
    # Remove common characters from both lists
    for char in s_list[:]:
        if char in t_list:
            s_list.remove(char)
            t_list.remove(char)
    
    # Convert remaining characters to sets
    s_set = set(s_list)
    t_set = set(t_list)
    
    # Find intersection and remove from both sets
    intersection = s_set.intersection(t_set)
    s_set -= intersection
    t_set -= intersection
    
    # If there are any characters in s_set that are not in t_set, return -1
    if len(s_set - t_set) != 0:
        return -1
    
    # Otherwise, return the number of unique insertions required
    return len(t_set - s_set)