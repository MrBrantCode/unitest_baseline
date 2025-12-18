"""
QUESTION:
Alisha has a string of length n. Each character is either 'a', 'b' or 'c'. She has to select two characters s[i] and s[j] such that s[i] != s[j] and i,j are valid indexes. She has to find the maximum value of the absolute difference between i and j i.e abs(i-j) .
Since Alisha is busy with her Semester exams help her find the maximum distance where distance is the maximum value of absolute difference between i and j  i.e abs(i-j) .

-----Input:-----
- The first and the only line contains the string s with each character either 'a', 'b', or 'c'. 

-----Output:-----
Print a single integer the maximum absolute difference between i and j. 

-----Constraints-----
- $1 \leq n \leq 10^5$
- s[i] can either be 'a', 'b' or 'c'.

-----Subtasks-----
- 40 points : $1 \leq n \leq 100$
- 60 points : $1 \leq n \leq 10^5$

-----Sample Input1:-----
aabcaaa

-----Sample Output1:-----
4

-----Sample Input2:-----
aba

-----Sample Output2:-----
1
"""

def find_max_distance(s: str) -> int:
    n = len(s)
    max_distance = 0
    
    # Store the first and last occurrence of each character
    first_occurrence = {'a': -1, 'b': -1, 'c': -1}
    last_occurrence = {'a': -1, 'b': -1, 'c': -1}
    
    for i in range(n):
        char = s[i]
        if first_occurrence[char] == -1:
            first_occurrence[char] = i
        last_occurrence[char] = i
    
    # Calculate the maximum distance between different characters
    for char1 in 'abc':
        for char2 in 'abc':
            if char1 != char2:
                if first_occurrence[char1] != -1 and first_occurrence[char2] != -1:
                    max_distance = max(max_distance, abs(first_occurrence[char1] - last_occurrence[char2]))
                    max_distance = max(max_distance, abs(last_occurrence[char1] - first_occurrence[char2]))
    
    return max_distance