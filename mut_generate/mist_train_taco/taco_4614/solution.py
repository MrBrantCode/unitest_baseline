"""
QUESTION:
Golu wants to find out the sum of Lucky numbers.Lucky numbers are those numbers which contain exactly two set bits.This task is very diffcult for him.So Help Golu to find sum of those numbers which exactly contain two set bits upto a given number N.

3 5 10 are lucky numbers where 7 14 are not.

INPUT First line contain number of test cases T.Each test case contains a single number N.
OUTPUT Print sum of all Lucky Numbers upto N.Output may be large so take modulo with 1000000007.  
Constraints 

1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^18

NOTE: Since value of test cases and n is really large, please use fast I/O optimization techniques. 

SAMPLE INPUT
1
5

SAMPLE OUTPUT
8
"""

def sum_of_lucky_numbers(n: int, mod: int = 1000000007) -> int:
    # Precompute the lucky numbers and their prefix sums
    bits = [2**e for e in range(64)]
    lucky = [-1]
    prefix_sum = [0]
    
    for i in range(1, 64):
        base = bits[i]
        for j in range(i):
            lucky.append(base + bits[j])
            prefix_sum.append((prefix_sum[-1] + lucky[-1]) % mod)
    
    # Binary search to find the largest lucky number <= n
    start = 0
    end = len(lucky) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        if lucky[mid] <= n and (mid == len(lucky) - 1 or lucky[mid + 1] > n):
            return prefix_sum[mid]
        if lucky[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0  # In case no lucky number is found (which shouldn't happen with valid input)