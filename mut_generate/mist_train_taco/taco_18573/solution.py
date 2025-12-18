"""
QUESTION:
Recently Rocky had participated in coding competition and he is sharing one of the problem with you which he was unable to solve. Help Rocky in solving the problem.
Suppose the alphabets are arranged in a row starting with index 0$0$ from AtoZ$A to Z$.
If in a coded language  A=27$A=27$ and AND=65$AND=65$.
Help Rocky to find a suitable formula for finding all the value for given test cases?
(All alphabets are in Upper case only).

-----Input:-----
First line of the input contains  string s$s$.

-----Output:-----
Output the possible integer values of the given string s$s$ according to the question . 

-----Constraints-----
- 1≤s≤100$1 \leq s \leq 100$

-----Sample Input:-----
A

AND   

-----Sample Output:-----
27

65
"""

def calculate_coded_value(s: str) -> int:
    start_w = 27
    w_dict = {}
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for word in words:
        w_dict[word] = start_w
        start_w -= 1
    
    total_wt = 0
    for c in s:
        total_wt += w_dict[c]
    
    return total_wt