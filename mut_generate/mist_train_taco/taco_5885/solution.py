"""
QUESTION:
The bustling town of Siruseri has just one sports stadium. There are a number of schools, colleges, sports associations, etc. that use this stadium as the venue for their sports events.
Anyone interested in using the stadium has to apply to the Manager of the stadium indicating both the starting date (a positive integer $S$) and the length of the sporting event in days (a positive integer $D$) they plan to organise. Since these requests could overlap it may not be possible to satisfy everyone. Also, there should be at least one gap day between any two approved events, so that the stadium can be cleaned.
It is the job of the Manager to decide who gets to use the stadium and who does not. The Manager, being a genial man, would like to keep as many organisations happy as possible and hence would like to allocate the stadium so that maximum number of events are held.
Suppose, for example, the Manager receives the following 4 requests:
$ $
Event No.   Starting Date        Length 

1                   2                    5
2                   9                    7
3                  15                    6
4                   9                    3

$ $ 
He would allot the stadium to events $1$, $4$ and $3$. Event $1$ begins on day $2$ and ends on day $6$, event $4$ begins on day $9$ and ends on day $11$ and event $3$ begins on day $15$ and ends on day $20$. You can verify that it is not possible to schedule all the $4$ events (since events $2$ and $3$ overlap and only one of them can get to use the stadium).
Your task is to help the manager find the best possible allotment (i.e., the maximum number of events that can use the stadium).

-----Input:-----
The first line of the input will contain a single integer $N$ indicating the number of events for which the Manager has received a request. Lines $2,3,...,N+1$ describe the requirements of the $N$ events. Line $i+1$ contains two integer $S_i$ and $D_i$ indicating the starting date and the duration of event $i$.

-----Output:-----
Your output must consist of a single line containing a single integer $M$, indicating the maximum possible number of events that can use the stadium.

-----Constraints:-----
- $1 \leq N \leq 100000$.
- $1 \leq S_i \leq 1000000$.
- $1 \leq D_i \leq 1000$.
- $50 \%$ of test cases will also satisfy $1 \leq N \leq 10000$.

-----Sample input:-----
4
2 5
9 7
15 6
9 3

-----Sample output:-----
3
"""

def max_events_scheduled(events):
    # Convert each event to a tuple of (start_date, end_date)
    events = [(S_i, S_i + D_i) for S_i, D_i in events]
    
    # Sort events by their end date
    events.sort(key=lambda event: event[1])
    
    # Initialize variables to track the last end date and the count of scheduled events
    last_end_date = -1
    scheduled_count = 0
    
    # Iterate through the sorted events
    for start_date, end_date in events:
        # If the current event starts after the last end date, schedule it
        if start_date > last_end_date:
            scheduled_count += 1
            last_end_date = end_date
    
    return scheduled_count