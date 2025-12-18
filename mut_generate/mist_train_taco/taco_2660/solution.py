"""
QUESTION:
Given a string S of '$'s and '.'s. '$' are planks on the bridge and '.'s are the broken sections of the bridge. You can jump up to only that much gap (number of '.') of the broken section which you have already jumped over previously otherwise it takes you 1 day to learn how to jump that far. You have to find how many days will you take to cross the bridge.
Example 1:
Input:
S = $$..$$...$.$
Output:
2
Explanation:
1 day is required to practice
for 2 dots.Then next time 3 
dots are encountered so 1 more
day to practice. Then since 1 
dot is there you can easily do
that because you have already 
mastered for 3 dots.
Example 2:
Input:
S = $$$$.$
Output:
1
Explanation:
Only one is required to learn
to jump 1 gap.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findDays() which takes the string S as input parameters and returns the total number of days you would take to cross the bridge.
 
Expected Time Complexity: O(|S|)
Expected Space Complexity: O(|S|)
 
Constraints:
1 ≤ T ≤ 100
1 ≤ |S| ≤ 10^{4}
S will consist of only the characters '$' and '.'
The first and the last characters of S will be '$'
"""

def find_days_to_cross_bridge(S: str) -> int:
    # Split the string by '$' to get the lengths of the broken sections
    broken_sections = map(len, S.split('$'))
    
    # Initialize variables to keep track of the maximum gap encountered and the days required
    max_gap = 0
    days_required = 0
    
    # Iterate through each broken section length
    for gap in broken_sections:
        if gap > max_gap:
            # If the current gap is larger than the maximum gap encountered so far,
            # it means we need an additional day to practice jumping this far
            days_required += 1
            max_gap = gap
    
    return days_required