"""
QUESTION:
Aureole the Techno-cultural fest of JEC thought of conducting a workshop on big data, as the topic is hot everyone wants to take part but due to limited seats in the Jashan Auditorium there is a selection criteria, a problem is given.
the problem states a string is to be compressed when two or more consecutive characters are same they are to be compressed into one character and the original number count is to be written after it ex. aaabb -> a3b2
where every character is of 8bits and every integer is of 32bits
you are asked to find the difference in size between original string and compressed string

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input $S$ the string to be compressed. 

-----Output:-----
For each testcase, output in a single line The difference in size.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq |S| \leq 10^5$

-----Subtasks-----
- 40 points : S will contain only a-z
- 60 points : S will contain 0-9 characters also

-----Sample Input:-----
1
aaabb

-----Sample Output:-----
-40

-----EXPLANATION:-----
the resulting string will be a3b2 its size will be 80, original string size will be 40 so ans= 40-80
"""

def calculate_compression_difference(S: str) -> int:
    n = len(S)
    
    if n == 1:
        if S[0].isalpha():
            return -32
        else:
            return 0
    
    num = 0
    ch = 0
    c = 1
    x = S[0]
    ans = ''
    
    for i in range(1, n):
        if S[i - 1] == S[i]:
            c += 1
            if i == n - 1:
                ans += S[i - 1]
                ch += 1
                if c > 1:
                    ans += str(c)
                    num += 1
                c = 1
        else:
            ans += S[i - 1]
            ch += 1
            if c > 1:
                ans += str(c)
                num += 1
            c = 1
            if i == n - 1:
                ans += S[i]
                ch += 1
    
    original_size = n * 8
    compressed_size = num * 32 + ch * 8
    difference = original_size - compressed_size
    
    return difference