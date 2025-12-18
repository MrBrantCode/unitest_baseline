"""
QUESTION:
Petya recieved a gift of a string s with length up to 10^5 characters for his birthday. He took two more empty strings t and u and decided to play a game. This game has two possible moves:  Extract the first character of s and append t with this character.  Extract the last character of t and append u with this character. 

Petya wants to get strings s and t empty and string u lexicographically minimal.

You should write a program that will help Petya win the game.


-----Input-----

First line contains non-empty string s (1 ≤ |s| ≤ 10^5), consisting of lowercase English letters.


-----Output-----

Print resulting string u.


-----Examples-----
Input
cab

Output
abc

Input
acdb

Output
abdc
"""

def lexicographically_minimal_string(s: str) -> str:
    s = list(s)
    s.reverse()
    t = []
    u = []
    s_cnt = [0] * (ord('z') + 1)
    
    for x in s:
        s_cnt[ord(x)] += 1
    
    def s_has_smaller(s_cnt_local, c):
        for i in range(ord('a'), ord(c)):
            if s_cnt_local[i] > 0:
                return True
        return False
    
    while s or t:
        if not s:
            while t:
                u.append(t.pop())
        elif not t:
            x = s.pop()
            s_cnt[ord(x)] -= 1
            t.append(x)
        elif s_has_smaller(s_cnt, t[-1]):
            x = s.pop()
            s_cnt[ord(x)] -= 1
            t.append(x)
        else:
            x = t.pop()
            u.append(x)
    
    return ''.join(u)