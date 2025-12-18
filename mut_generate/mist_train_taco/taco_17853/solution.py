"""
QUESTION:
Watson gives to Sherlock two strings S1 and S2 consisting of uppercase English alphabets. Next he wants Sherlock to build a flower in the following way:

He puts both strings perpendicular to each other in such a way that they overlap at the same character. For example, if he has two strings "ABCDEF" and "XXBCZQ", one possible way to make a flower is:

Length of petals in the above flower are 2, 2, 3 and 3.
A flower's ugliness is sum of absolute difference of adjacent petal lengths i.e. i.e. if adjacent petal lengths are L1, L2, L3, L4, then ugliness of flower is |L1 - L2| + |L2 - L3| + |L3 - L4| + |L4 - L1|. 
Sherlock wants to find minimum value of ugliness if we consider all possible flower configurations. Note that a configuration is valid even if any of the petal length is 0.

-----Input-----
First line contains T, number of test cases. Each test case consists of string S1 in one line followed by string S2 in the next line. It is guaranteed that there exists at least one possible way to make a flower.

-----Output-----
For each test case, output in one line the required answer.

-----Constraints-----
- 1 ≤ T ≤ 10
- 1 ≤ length(S1), length(S2) ≤ 105

-----Example-----
Input:
2
ABCDE
XXBCZQ
BBB
BBBBBB

Output: 
2
6

-----Explanation-----

Test case 1:

If we keep the configuration shown in statement, the ugliness is 2, which is minimum possible.

Test case 2:

One of the best configurations is

B 
B B B  B  B B
B

where petal lengths are 1, 3, 1, 2.
"""

def calculate_minimum_ugliness(S1: str, S2: str) -> int:
    m1 = len(S1) / 2
    m2 = len(S2) / 2
    
    d1 = {}
    d2 = {}
    
    # Populate d1 with the minimum distance from the center for each character in S1
    for i in range(len(S1)):
        c = S1[i]
        v = abs(m1 - i)
        if c in d1:
            if v < d1[c][0]:
                d1[c] = [v, i]
        else:
            d1[c] = [v, i]
    
    # Populate d2 with the minimum distance from the center for each character in S2
    for i in range(len(S2)):
        c = S2[i]
        v = abs(m2 - i)
        if c in d2:
            if v < d2[c][0]:
                d2[c] = [v, i]
        else:
            d2[c] = [v, i]
    
    mini = float('inf')
    
    # Calculate the minimum ugliness
    for i in d1:
        if i in d2:
            L1 = d1[i][1]
            L3 = len(S1) - L1 - 1
            L2 = d2[i][1]
            L4 = len(S2) - L2 - 1
            v = abs(L1 - L2) + abs(L2 - L3) + abs(L3 - L4) + abs(L4 - L1)
            if v < mini:
                mini = v
    
    return mini