"""
QUESTION:
Given a time in the format of hh:mm (12-hour format) 0 < HH < 12, 0 <= MM < 60. The task is to convert it into words.
Note: There are different corner cases appears for simplicity refer this example:
6:00 six o'clock
6:10 ten minutes past six
6:15 quarter past six
6:30 half past six
6:45 quarter to seven
6:47 thirteen minutes to seven
Example 1:
Input: H = 6, M = 0
Output: six o' clock
Explanation: 6H:0M = six o' clock.
Example 2:
Input: N = 6, M = 10
Output: ten minutes past six
Explanation: 6H:10M = ten minutes past six.
Your Task:  
You dont need to read input or print anything. Complete the function timeToWord() which takes H and M as input parameter and returns words converted from given time.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(k^{2})
Constraints:
0 < H < 12
0= < M < 60
"""

def time_to_word(H, M):
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
    
    if M == 0:
        return f"{nums[H]} o' clock"
    elif M == 1:
        return f"one minute past {nums[H]}"
    elif M == 59:
        return f"one minute to {nums[(H % 12) + 1]}"
    elif M == 15:
        return f"quarter past {nums[H]}"
    elif M == 30:
        return f"half past {nums[H]}"
    elif M == 45:
        return f"quarter to {nums[(H % 12) + 1]}"
    elif M < 30:
        return f"{nums[M]} minutes past {nums[H]}"
    elif M > 30:
        return f"{nums[60 - M]} minutes to {nums[(H % 12) + 1]}"