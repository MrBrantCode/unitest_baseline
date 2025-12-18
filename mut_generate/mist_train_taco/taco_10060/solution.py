"""
QUESTION:
Given a string with repeated characters, the task is to complete the function rearrangeString which rearrange characters in a string so that no two adjacent characters are same.
Note : It may be assumed that the string has only lowercase English alphabets and such transformation is always always possible.
Example 1:
Input:
S = aaabc
Output: 1
Explanation: We can transform the string
to abaca.
Example 2:
Input:
S = aaabb
Output: 1
Explanation: We can transform the string
to ababa.
 
Your Task:
Complete the function rearrangeString() which takes a string as an input parameter and returns the rearranged string. (The output will be 1 if the returned string has no adjacent character same, otherwise 0. Printing is done by the driver's code.)
Expected Time Complexity: O(N * log N), N = length of the string.
Expected Auxiliary Space: O(constant)
Constraints:
1< N < 10^{5}
"""

from heapq import *

def rearrange_string(string):
    n = len(string)
    count = [0] * 26
    
    # Count the frequency of each character
    for char in string:
        count[ord(char) - 97] += 1
    
    pq = []
    res = ''
    
    # Push the characters with their negative counts into the priority queue
    for i in range(97, 123):
        if count[i - 97] != 0:
            heappush(pq, [-1 * count[i - 97], chr(i)])
    
    prev = [1, '#']
    
    # Rearrange the string
    while pq:
        ky = heappop(pq)
        res += ky[1]
        
        if prev[0] < 0:
            heappush(pq, prev)
        
        ky[0] += 1
        prev = ky
    
    # If the length of the result is not equal to the input string length, return -1
    if len(res) != n:
        return '-1'
    
    return res