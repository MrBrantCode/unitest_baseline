"""
QUESTION:
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
 
Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

 
Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""

from collections import defaultdict

def max_balloon_instances(text: str) -> int:
    memo = defaultdict(int)
    for char in text:
        if char in 'balon':
            memo[char] += 1
    
    count_once = min(memo['b'], memo['a'], memo['n'])
    count_twice = min(memo['l'], memo['o'])
    
    return min(count_once, count_twice // 2)