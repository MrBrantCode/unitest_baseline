"""
QUESTION:
Vitaly is a diligent student who never missed a lesson in his five years of studying in the university. He always does his homework on time and passes his exams in time. 

During the last lesson the teacher has provided two strings s and t to Vitaly. The strings have the same length, they consist of lowercase English letters, string s is lexicographically smaller than string t. Vitaly wondered if there is such string that is lexicographically larger than string s and at the same is lexicographically smaller than string t. This string should also consist of lowercase English letters and have the length equal to the lengths of strings s and t. 

Let's help Vitaly solve this easy problem!

Input

The first line contains string s (1 ≤ |s| ≤ 100), consisting of lowercase English letters. Here, |s| denotes the length of the string.

The second line contains string t (|t| = |s|), consisting of lowercase English letters.

It is guaranteed that the lengths of strings s and t are the same and string s is lexicographically less than string t.

Output

If the string that meets the given requirements doesn't exist, print a single string "No such string" (without the quotes).

If such string exists, print it. If there are multiple valid strings, you may print any of them.

Examples

Input

a
c


Output

b


Input

aaa
zzz


Output

kkk


Input

abcdefg
abcdefh


Output

No such string

Note

String s = s1s2... sn is said to be lexicographically smaller than t = t1t2... tn, if there exists such i, that s1 = t1, s2 = t2, ... si - 1 = ti - 1, si < ti.
"""

def find_lexicographical_string(s: str, t: str) -> str:
    """
    Finds a string that is lexicographically larger than `s` and smaller than `t`.
    
    Parameters:
    s (str): The first string, lexicographically smaller than `t`.
    t (str): The second string, lexicographically larger than `s`.
    
    Returns:
    str: A string that is lexicographically between `s` and `t`, or "No such string" if no such string exists.
    """
    
    def increment_string(s):
        if s[-1] == 'z':
            return increment_string(s[:-1]) + 'a'
        else:
            return s[:-1] + chr(ord(s[-1]) + 1)
    
    candidate = increment_string(s)
    if candidate < t:
        return candidate
    else:
        return "No such string"