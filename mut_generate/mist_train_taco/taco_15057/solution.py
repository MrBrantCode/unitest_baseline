"""
QUESTION:
In a native language, the increasing order of priority of characters is a, b, c, d, e, f, g, h, i, j, k, l, m, n, ng, o, p, q, r, s, t, u, v, w, x, y, z. You are given two strings s1 and s2 and your task is to compare them on the basis of the given priority order.
Note: Function must return 0 if both the strings are equal, 1 if s1 is greater than s2, and -1 if s1 is lesser than s2.
Example 1:
Input: s1 = "adding", s2 = "addio"
Output: -1
Explanation: 'o' has greater priority 
than 'ng'
Example 2:
Input: s1 = "abcng", s2 = "abcno"
Output: 1
Explanation: 'ng' has greater priority 
than 'n'
Your Task:  
You don't need to read input or print anything. Your task is to complete the function stringComparsion() which takes the two strings as input and returns the integer value.
Expected Time Complexity: O(|s1 + s2|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |s1|, |s2| ≤ 105
The string contains lower case English alphabets
"""

def compare_strings(s1: str, s2: str) -> int:
    priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
                'k': 11, 'l': 12, 'm': 13, 'n': 14, 'ng': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 
                's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27}
    
    i = 0
    while i < min(len(s1), len(s2)):
        if s1[i] == 'n' and i + 1 < len(s1) and s1[i + 1] == 'g':
            s1_priority = priority['ng']
            if s2[i] == 'n' and i + 1 < len(s2) and s2[i + 1] == 'g':
                s2_priority = priority['ng']
                i += 2
            else:
                s2_priority = priority[s2[i]]
                i += 1
        elif s2[i] == 'n' and i + 1 < len(s2) and s2[i + 1] == 'g':
            s2_priority = priority['ng']
            s1_priority = priority[s1[i]]
            i += 1
        else:
            s1_priority = priority[s1[i]]
            s2_priority = priority[s2[i]]
            i += 1
        
        if s1_priority > s2_priority:
            return 1
        elif s1_priority < s2_priority:
            return -1
    
    if len(s1) > len(s2):
        return 1
    elif len(s2) > len(s1):
        return -1
    
    return 0