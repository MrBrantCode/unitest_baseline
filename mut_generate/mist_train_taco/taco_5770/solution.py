"""
QUESTION:
DZY has a sequence a, consisting of n integers.

We'll call a sequence a_{i}, a_{i} + 1, ..., a_{j} (1 ≤ i ≤ j ≤ n) a subsegment of the sequence a. The value (j - i + 1) denotes the length of the subsegment.

Your task is to find the longest subsegment of a, such that it is possible to change at most one number (change one number to any integer you want) from the subsegment to make the subsegment strictly increasing.

You only need to output the length of the subsegment you find.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5). The next line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).


-----Output-----

In a single line print the answer to the problem — the maximum length of the required subsegment.


-----Examples-----
Input
6
7 2 3 1 5 6

Output
5



-----Note-----

You can choose subsegment a_2, a_3, a_4, a_5, a_6 and change its 3rd element (that is a_4) to 4.
"""

def find_longest_increasing_subsegment_length(n, sequence):
    if n == 1:
        return 1
    
    leftList = [1] * n
    rightList = [1] * n
    ans = 0
    
    # Calculate leftList
    for i in range(1, n):
        if sequence[i - 1] < sequence[i]:
            leftList[i] = leftList[i - 1] + 1
        ans = max(ans, leftList[i])
    
    # If the longest increasing subsegment is the entire sequence, we can only change one element
    if ans < n:
        ans += 1
    
    # Calculate rightList
    for i in range(n - 2, -1, -1):
        if sequence[i + 1] > sequence[i]:
            rightList[i] = rightList[i + 1] + 1
    
    # Check for the possibility of changing one element to make a longer subsegment
    for i in range(1, n - 1):
        if sequence[i + 1] - sequence[i - 1] >= 2:
            ans = max(ans, leftList[i - 1] + 1 + rightList[i + 1])
    
    return ans