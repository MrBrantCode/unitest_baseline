"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 

Mike likes strings. He is also interested in algorithms. A few days ago he discovered for himself a very nice problem:

You are given an AB-string S. You need to count the number of substrings of S, which have an equal number of 'A'-s and 'B'-s.

Do you know how to solve it? Good. Mike will make the problem a little bit more difficult for you.

You are given an ABC-string S. You need to count the number of substrings of S, which have an equal number of 'A'-s, 'B'-s and 'C'-s.

A string is called AB-string if it doesn't contain any symbols except 'A' or 'B'. A string is called ABC-string if it doesn't contain any symbols except 'A', 'B' or 'C'.

------ Input ------ 

The first line of the input contains an ABC-string S.

------ Output ------ 

Your output should contain the only integer, denoting the number of substrings of S, which have an equal number of 'A'-s, 'B'-s and 'C'-s.

The answer can go above a 32-bit integer. Please, use 64-bit integers for storing and processing data.

------ Constraints ------ 

1 ≤ |S| ≤  1 000 000; where |S| denotes the length of the given ABC-string.

------ Example ------ 

Input:
ABACABA

Output:
2

------ Explanation ------ 

In the example you should count S[2..4] = "BAC" and S[4..6] = "CAB".
"""

def count_balanced_substrings(s: str) -> int:
    a, b, c = 0, 0, 0
    ans = 0
    dict = {}
    dict[(0, 0)] = 1
    
    for char in s:
        if char == 'A':
            a += 1
        elif char == 'B':
            b += 1
        elif char == 'C':
            c += 1
        
        k = (c - a, c - b)
        if k in dict:
            ans += dict[k]
            dict[k] += 1
        else:
            dict[k] = 1
    
    return ans