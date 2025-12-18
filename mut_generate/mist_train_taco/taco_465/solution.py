"""
QUESTION:
There are several days left before the fiftieth birthday of a famous Berland's writer Berlbury. In this connection the local library decided to make an exposition of the works of this famous science-fiction writer. It was decided as well that it is necessary to include into the exposition only those books that were published during a particular time period. It is obvious that if the books differ much in size, the visitors will not like it. That was why the organizers came to the opinion, that the difference between the highest and the lowest books in the exposition should be not more than k millimeters.

The library has n volumes of books by Berlbury, arranged in chronological order of their appearance. The height of each book in millimeters is know, it is hi. As Berlbury is highly respected in the city, the organizers want to include into the exposition as many books as possible, and to find out what periods of his creative work they will manage to cover. You are asked to help the organizers cope with this hard task.

Input

The first line of the input data contains two integer numbers separated by a space n (1 ≤ n ≤ 105) and k (0 ≤ k ≤ 106) — the amount of books by Berlbury in the library, and the maximum allowed height difference between the lowest and the highest books. The second line contains n integer numbers separated by a space. Each number hi (1 ≤ hi ≤ 106) is the height of the i-th book in millimeters.

Output

In the first line of the output data print two numbers a and b (separate them by a space), where a is the maximum amount of books the organizers can include into the exposition, and b — the amount of the time periods, during which Berlbury published a books, and the height difference between the lowest and the highest among these books is not more than k milllimeters.

In each of the following b lines print two integer numbers separated by a space — indexes of the first and the last volumes from each of the required time periods of Berlbury's creative work.

Examples

Input

3 3
14 12 10


Output

2 2
1 2
2 3


Input

2 0
10 10


Output

2 1
1 2


Input

4 5
8 19 10 13


Output

2 1
3 4
"""

from collections import deque

def mini_in_window(A, n, k):
    d = deque()
    res = []
    for i in range(n):
        if i >= k and d[0] == i - k:
            d.popleft()
        while len(d) and A[d[-1]] >= A[i]:
            d.pop()
        d.append(i)
        if i >= k - 1:
            res.append(d[0])
    return res

def maxi_in_window(A, n, k):
    d = deque()
    res = []
    for i in range(n):
        if i >= k and d[0] == i - k:
            d.popleft()
        while len(d) and A[d[-1]] <= A[i]:
            d.pop()
        d.append(i)
        if i >= k - 1:
            res.append(d[0])
    return res

def find_optimal_exposition_periods(n, k, heights):
    l = 0
    r = n + 1
    maxans = 0
    cntmax = []
    
    while l + 1 < r:
        mid = (l + r) // 2
        if mid > maxans:
            cntnow = []
            mins = mini_in_window(heights, n, mid)
            maxes = maxi_in_window(heights, n, mid)
            for i in range(len(mins)):
                if heights[maxes[i]] - heights[mins[i]] <= k:
                    cntnow.append((mins[i] + 1, maxes[i] + 1))
            if cntnow:
                l = mid
                cntmax = cntnow[:]
            else:
                r = mid
    
    max_books = l
    periods = cntmax
    
    return max_books, periods