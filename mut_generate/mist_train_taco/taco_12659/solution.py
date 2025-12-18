"""
QUESTION:
You are given an array $a$ consisting of $n$ integers numbered from $1$ to $n$.

Let's define the $k$-amazing number of the array as the minimum number that occurs in all of the subsegments of the array having length $k$ (recall that a subsegment of $a$ of length $k$ is a contiguous part of $a$ containing exactly $k$ elements). If there is no integer occuring in all subsegments of length $k$ for some value of $k$, then the $k$-amazing number is $-1$.

For each $k$ from $1$ to $n$ calculate the $k$-amazing number of the array $a$.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases. Then $t$ test cases follow.

The first line of each test case contains one integer $n$ ($1 \le n \le 3 \cdot 10^5$) — the number of elements in the array. The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le n$) — the elements of the array. 

It is guaranteed that the sum of $n$ over all test cases does not exceed $3 \cdot 10^5$.


-----Output-----

For each test case print $n$ integers, where the $i$-th integer is equal to the $i$-amazing number of the array.


-----Example-----
Input
3
5
1 2 3 4 5
5
4 4 4 4 2
6
1 3 1 5 3 1

Output
-1 -1 3 2 1 
-1 4 4 4 2 
-1 -1 1 1 1 1
"""

def calculate_k_amazing_numbers(test_cases):
    results = []
    
    for n, a in test_cases:
        a = [0] + a  # Adjusting the array to start from index 1
        period = [0] * (n + 1)
        first = [-1] * (n + 1)
        last = [-1] * (n + 1)
        
        # Calculate the first and last occurrences and the maximum period for each element
        for i in range(1, len(a)):
            b = a[i]
            if first[b] == -1:
                first[b] = i
                last[b] = i
            else:
                period[b] = max(period[b], i - last[b])
                last[b] = i
        
        # Adjust the period for the last occurrence of each element
        for i in range(1, len(period)):
            period[i] = max(period[i], n - last[i] + 1)
        
        period = period[1:]  # Remove the first element which is not needed
        
        # Create a list of tuples (period, element) and sort it
        l = sorted((e if e[0] > first[e[1]] else (first[e[1]], e[1]) for e in zip(period, list(range(1, n + 1))) if e[0] > 0))
        
        ans = []
        AA = n + 5
        ind = 0
        
        # Calculate the k-amazing numbers
        for i in range(1, n + 1):
            if ind < len(l) and l[ind][0] == i:
                AA = min(AA, l[ind][1])
            ans.append(-1 if AA == n + 5 else AA)
            while ind < len(l) and l[ind][0] == i:
                ind += 1
        
        results.append(ans)
    
    return results