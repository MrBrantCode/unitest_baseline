"""
QUESTION:
Given a string S of length N consisting of only lower-case English alphabets, you will be asked to process Q queries over it . In each query you will be given two lower case characters X and Y. Your task is to find out the number of such substrings of the the string S which have the characters X  and Y on either of its  end points, both  X...Y  and Y...X are considered to be valid. 

Note :  Substrings length should be greater than 1. 
Input:
The first line of the input will contain N  , the length of the string. 
Next line will contain as string of length N. 
Next line will will contain Q , the number of queries. Then Q subsequent lines will contain two lowercase characters X and Y separated by a space.

Output:
For each query , output the answer in a separate line.   

Constraints:

1 ≤ N ≤ 10^6
1 ≤ Q ≤ 10^3

SAMPLE INPUT
5
aacbb
2
a c
a b

SAMPLE OUTPUT
2
4

Explanation

For the first query, the possible substrings are aac and ac . Hence the answer is 2. 
For the second query, the possible substrings are aacbb  ,  aacb ,  acbb , and acb , hence making a total of 4 substrings.
"""

def count_substrings_with_endpoints(S, queries):
    from collections import defaultdict
    import string

    # Length of the string
    N = len(S)
    
    # Count occurrences of each character in the string
    count = {x: S.count(x) for x in string.ascii_lowercase}
    
    # Map each character to its indices in the string
    mmap = defaultdict(list)
    for i, x in enumerate(S):
        mmap[x].append(i)
    
    results = []
    
    for X, Y in queries:
        if X == Y:
            # If X and Y are the same, the number of valid substrings is the combination of choosing 2 out of count[X]
            results.append((count[X] * (count[X] - 1)) // 2)
        else:
            # If X and Y are different, the number of valid substrings is the product of their counts
            results.append(count[X] * count[Y])
    
    return results