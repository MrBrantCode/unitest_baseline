"""
QUESTION:
They declared Sonam as bewafa. Although she is not, believe me! She asked a number of queries to people regrading their position in a test. Now its your duty to remove her bewafa tag by answering simple queries. All the students who give test can score from 1 to 10^18. Lower the marks, better the rank. Now instead of directly telling the marks of student they have been assigned groups where marks are distributed in continuous intervals, you have been given l(i) lowest mark of interval i and r(i) highest marks in interval i. So marks distribution in that interval is given as l(i), l(i)+1, l(i)+2 . . . r(i).
Now Sonam ask queries in which she gives rank of the student (rank_{i}) and you have to tell marks obtained by that student. Simply, for each query output marks obtain by student whose rank is rank_{i}(1<=rank_{i}<=10^{18}).
Note: rank1 is better than rank2 and rank2 is better than rank3 and so on and the first interval starts from 1.
Example 1:
Input:
n=3, q=3 
l[] = {1, 12, 22} 
r[] = {10, 20, 30} 
rank[] = {5, 15, 25}
Output:
5 16 27
Intervals are from 1 to 10, second
interval from 12 to 20 and third 22 to 30.
In this test case, from 1 to 10 , they
are given the ranks from 1 to 10 but
in the second interval, it is starting
from 12 , so we will have to give its rank
11 and so on like this.
Rank:    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15......
Marks: 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16.....
So 5th rank will score 5 marks,15th rank will
score 16 marks and 25th rank will score 27 marks.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getTestMarks() which takes the array l[], r[], its size n and array rank[], StoreAnswer[], its size q as inputs and fill the StoreAnswer[] array. This array stores the answer of every query.
Expected Time Complexity: O(n. log(n))
Expected Auxiliary Space: O(n.q)
Constraints:
1<=n<=10^{5}
1<=q<=10^{5}
1<= l(i) < r(i) <=10^{18}
1<=rank_{i}<=10^{18}
"""

def get_test_marks(n, q, l, r, rank):
    # Initialize the list to store the answers
    store_answer = [0] * q
    
    # Create a list of intervals with their respective ranges
    intervals = [(l[i], r[i]) for i in range(n)]
    
    # Sort the intervals based on the starting marks
    intervals.sort()
    
    # Calculate the cumulative count of students in each interval
    cnt = []
    for i in range(n):
        curr = intervals[i][1] - intervals[i][0] + 1
        if i == 0:
            cnt.append(curr)
        else:
            cnt.append(cnt[i - 1] + curr)
    
    # Process each query
    for i in range(q):
        lo, hi = 0, n - 1
        ans = -1
        
        # Binary search to find the interval containing the rank
        while lo <= hi:
            mi = (lo + hi) // 2
            if cnt[mi] >= rank[i]:
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        
        # Calculate the marks based on the found interval
        if ans == -1:
            store_answer[i] = intervals[n - 1][1] + rank[i] - cnt[n - 1]
        else:
            before = cnt[ans - 1] if ans > 0 else 0
            store_answer[i] = rank[i] - before + intervals[ans][0] - 1
    
    return store_answer