"""
QUESTION:
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.

If there is no such string s return the empty string "".
 
Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

 
Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""

import heapq

def generate_longest_happy_string(a: int, b: int, c: int) -> str:
    if a == 0 and b == 0 and c == 0:
        return ''
    
    res = ''
    heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
    heapq.heapify(heap)
    prev_val = 0
    prev_char = ''
    
    while heap:
        (v, char) = heapq.heappop(heap)
        if prev_val < 0:
            heapq.heappush(heap, (prev_val, prev_char))
        
        if abs(v) >= 2:
            if abs(v) > abs(prev_val):
                res += char * 2
                v += 2
            else:
                res += char
                v += 1
        elif abs(v) == 1:
            res += char
            v += 1
        elif abs(v) == 0:
            break
        
        prev_val = v
        prev_char = char
    
    return res