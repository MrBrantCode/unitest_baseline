"""
QUESTION:
Let's call a string "s-palindrome" if it is symmetric about the middle of the string. For example, the string "oHo" is "s-palindrome", but the string "aa" is not. The string "aa" is not "s-palindrome", because the second half of it is not a mirror reflection of the first half.

 [Image] English alphabet 

You are given a string s. Check if the string is "s-palindrome".


-----Input-----

The only line contains the string s (1 ≤ |s| ≤ 1000) which consists of only English letters.


-----Output-----

Print "TAK" if the string s is "s-palindrome" and "NIE" otherwise.


-----Examples-----
Input
oXoxoXo

Output
TAK

Input
bod

Output
TAK

Input
ER

Output
NIE
"""

def is_s_palindrome(s: str) -> str:
    chars = {
        'A': {'A'}, 'b': {'d'}, 'd': {'b'}, 'H': {'H'}, 'M': {'M'}, 'O': {'O'}, 
        'o': {'o'}, 'T': {'T'}, 'U': {'U'}, 'V': {'V'}, 'v': {'v'}, 'W': {'W'}, 
        'w': {'w'}, 'X': {'X'}, 'x': {'x'}, 'Y': {'Y'}, 'q': {'p'}, 'p': {'q'}, 
        'I': {'I'}
    }
    not_clean = {'p', 'q', 'b', 'd'}
    
    ans = True
    for i in range(len(s) // 2):
        if s[i] not in chars.keys() or s[len(s) - i - 1] not in chars[s[i]]:
            ans = False
            break
    
    if len(s) % 2 != 0 and (s[len(s) // 2] not in chars.keys() or s[len(s) // 2] in not_clean):
        ans = False
    
    return "TAK" if ans else "NIE"