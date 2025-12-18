"""
QUESTION:
G: Working

Kou decided to do the same number of jobs every day for the next $ N $.

$ A_i $ jobs are added on the $ i $ day of the $ N $ day.

Mr. Kou has no work to do now, and he doesn't have to finish all the work by the $ N $ day.

How many jobs can you do in a day?

However, Mr. Kou is excellent, so he can do as many jobs as he has.

input

$ N $ is given on the first line.

On the second line, $ N $ integers $ A_1, A_2, A_3, \ dots, A_N $ are given, separated by blanks.

output

Output the maximum number of jobs you can do in a day. Insert a line break at the end.

Constraint

* $ N $ is an integer greater than or equal to $ 1 $ and less than or equal to $ 100 $
* $ A_1, A_2, A_3, \ dots, A_N $ are integers between $ 1 $ and $ 100 $



Input example 1


Five
4 2 5 3 1


Output example 1


3


If you decide to work more than $ 4 $ a day, you'll run out of work on the second day.

Input example 2


Five
9 9 1 9 9


Output example 2


6






Example

Input

5
4 2 5 3 1


Output

3
"""

from itertools import accumulate

def calculate_max_daily_jobs(N, A):
    # Calculate the cumulative sum of jobs added each day
    cumulative_jobs = list(accumulate(A))
    
    # Iterate from 100 down to 1 to find the maximum jobs that can be done daily
    for i in range(100, 0, -1):
        for j in range(N):
            if i * (j + 1) > cumulative_jobs[j]:
                break
        else:
            return i

# Example usage:
# result = calculate_max_daily_jobs(5, [4, 2, 5, 3, 1])
# print(result)  # Output: 3