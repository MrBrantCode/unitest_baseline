"""
QUESTION:
Given two dates, find the total number of days between them.
Note: The system follows Gregorian calender from the beginning of time.
 
Example 1:
Input:
d1 = 10, m1 = 2, y1 = 2014
d2 = 10, m2 = 3, y2 = 2015
Output:
393
Explanation:
By counting manually, we find out there
are 393 days between the two dates.
Example 2:
Input:
d1 = 10, m1 = 2, y1 = 2001
d2 = 10, m2 = 2, y2 = 2002
Output:
365
Explanation:
By counting manually, we find out there
are 365 days between the two dates.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfDays() which takes Integers d1,m1,y1 for the first date and d2,m2,y2 as the second date as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= d1,d2 <= 31
1 <= m1,m2 <= 12
1 <= y1,y2 <= 3000
"""

from datetime import date

def calculate_days_between_dates(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    date1 = date(y1, m1, d1)
    date2 = date(y2, m2, d2)
    if date2 > date1:
        delta = date2 - date1
    else:
        delta = date1 - date2
    return delta.days