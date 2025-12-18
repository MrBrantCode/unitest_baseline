"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef is a well-known chef, and everyone wishes to taste his dishes.

As you might know, cooking is not an easy job at all and cooking everyday makes the chef very tired. So, Chef has decided to give himself some days off.

Chef has made a schedule for the next N days: On i-th day if A_{i} is equal to 1 then Chef is going to cook a delicious dish on that day, if A_{i} is equal to 0 then Chef is going to rest on that day.

After Chef made his schedule he discovered that it's not the best schedule, because there are some big blocks of consecutive days where Chef will cook which means it's still tiring for Chef, and some big blocks of consecutive days where Chef is going to rest which means chef will be bored doing nothing during these days.

Which is why Chef has decided to make changes to this schedule, but since he doesn't want to change it a lot, he will flip the status of at most K days. So for each day which Chef chooses, he will make it 1 if it was 0 or he will make it 0 if it was 1.

Help Chef by writing a program which flips the status of at most K days so that the size of the maximum consecutive block of days of the same status is minimized.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases.

The first line of each test case contains two integers: N denoting the number of days and K denoting maximum number of days to change.

The second line contains a string of length N , of which the i-th character is 0 if chef is going to rest on that day, or 1 if chef is going to work on that day

------ Output ------ 

For each test case, output a single line containing a single integer, which is the minimum possible size of maximum block of consecutive days of the same status achievable.

------ Constraints ------ 

1 ≤ T ≤ 11,000
1 ≤ N ≤ 10^{6}
The sum of N in all test-cases won't exceed 10^{6}.
0 ≤ K ≤ 10^{6}
0 ≤ A_{i} ≤ 1

------ Subtasks ------ 

Subtask #1 (20 points): N ≤ 10
Subtask #2 (80 points): Original Constraints 

----- Sample Input 1 ------ 
2
9 2
110001111
4 1
1001
----- Sample Output 1 ------ 
2
2
----- explanation 1 ------ 
Example case 1: The answer is 2 because we can change the string to: 110101011
Example case 2: If we don't change the input string at all, the answer will be 2. It is the best value we can achieve under the given conditions.
"""

def minimize_max_consecutive_block(N, K, schedule):
    # Helper function to count the number of flips needed to make the schedule alternating
    def count_flips(pattern):
        flips = 0
        for i in range(N):
            if pattern[i] != schedule[i]:
                flips += 1
        return flips

    # Generate two alternating patterns
    a = '01' * (N // 2)
    b = '10' * (N // 2)
    if N % 2 == 1:
        a += '0'
        b += '1'

    # Count the number of flips needed for each pattern
    n1 = count_flips(a)
    n2 = count_flips(b)

    # If either pattern can be achieved with at most K flips, the answer is 1
    if n1 <= K or n2 <= K:
        return 1

    # Otherwise, find the minimum possible size of the maximum block
    blocks = []
    count = 1
    for i in range(1, N):
        if schedule[i] != schedule[i - 1]:
            blocks.append(count)
            count = 1
        else:
            count += 1
    blocks.append(count)

    # Binary search to find the minimum size of the maximum block
    l, r = 2, N
    while l < r:
        mid = (l + r) // 2
        c = 0
        for i in blocks:
            if i > mid:
                c += i // (mid + 1)
        if c > K:
            l = mid + 1
        else:
            r = mid

    return l