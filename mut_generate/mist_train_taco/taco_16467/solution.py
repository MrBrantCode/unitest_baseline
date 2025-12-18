"""
QUESTION:
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago. 

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format: 

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.  

Input Format

The first line contains $\mathbf{T}$, the number of testcases. 

Each testcase contains $2$ lines, representing time $\boldsymbol{t_1}$ and time $t_2$. 

Constraints

Input contains only valid timestamps
$year\:\leq3000$. 

Output Format

Print the absolute difference $(t_1-t_2)$ in seconds.  

Sample Input 0
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output 0
25200
88200

Explanation 0

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is $7\times3600$ seconds or $25200$ seconds.  

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or $24\times3600+30\times60\Rightarrow88200$
"""

from datetime import datetime

def calculate_time_difference(t1: str, t2: str) -> int:
    """
    Calculate the absolute difference in seconds between two timestamps.

    Parameters:
    t1 (str): The first timestamp in the format 'Day dd Mon yyyy hh:mm:ss +xxxx'.
    t2 (str): The second timestamp in the same format.

    Returns:
    int: The absolute difference in seconds between the two timestamps.
    """
    time_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the timestamps
    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)
    
    # Calculate the absolute difference in seconds
    difference_in_seconds = int(abs((time2 - time1).total_seconds()))
    
    return difference_in_seconds