"""
QUESTION:
Given a month with arbitrary number of days, N, and an integer K representing the day with which it starts. ie- 1 for Monday, 2 for Tuesday and so on.  Find the number of times each day (Monday, Tuesday, ..., Sunday) appears in the month. 
 
Example 1:
Input:
N = 31 , K = 1
Output:
5 5 5 4 4 4 4 
Explanation: The month starts from Monday.
There will be 4 days of each day
(Sunday , Monday , etc) upto 28th of the
Month. Then, The successive 3 days will
have a extra day each. So, Monday, Tuesday
and Wednesday will have 5 days while the
others will have 4 days each.
Example 2:
Input:
N = 28, K = 5
Output:
5 5 5 4 4 4 4 
Explanation: Each day of the month will
have 4 days each and thus the Output.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function daysOfWeeks() which takes Integers N  and K as input and return a list of 7 integers indicating number of days in each day of the week.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
1 <= K <= 7
"""

def days_of_weeks(N: int, K: int) -> list[int]:
    # Initialize the list with the base number of days for each week day
    days_count = [N // 7] * 7
    
    # Calculate the remaining days after evenly distributing the days
    remaining_days = N % 7
    
    # Distribute the remaining days starting from the given day K
    for i in range(remaining_days):
        day_index = (K - 1 + i) % 7
        days_count[day_index] += 1
    
    return days_count