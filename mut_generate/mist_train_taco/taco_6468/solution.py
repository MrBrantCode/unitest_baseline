"""
QUESTION:
Given a string str of length N which consists of only 0, 1 or 2s, count the number of substring which have equal number of 0s, 1s and 2s.
 
Example 1:
Input: str = “0102010”
Output: 2
Explanation: Substring str[2, 4] = “102” and
substring str[4, 6] = “201” has equal number
of 0, 1 and 2 
Example 2:
Input: str = “11100022”
Output: 0
Explanation: There is no substring with
equal number of 0 , 1 and 2.
Your Task:  
You don't need to read input or print anything.Your task is to complete the function getSubstringWithEqual012() which takes a single string str as input and returns the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def count_substrings_with_equal_012(str):
    n = len(str)
    hash_map = {(0, 0): 1}
    count = [0, 0, 0]
    result = 0
    
    for i in range(n):
        count[int(str[i])] += 1
        temp = (count[0] - count[1], count[1] - count[2])
        
        if temp in hash_map:
            result += hash_map[temp]
            hash_map[temp] += 1
        else:
            hash_map[temp] = 1
    
    return result