"""
QUESTION:
Some natural number was written on the board. Its sum of digits was not less than k. But you were distracted a bit, and someone changed this number to n, replacing some digits with others. It's known that the length of the number didn't change.

You have to find the minimum number of digits in which these two numbers can differ.


-----Input-----

The first line contains integer k (1 ≤ k ≤ 10^9).

The second line contains integer n (1 ≤ n < 10^100000).

There are no leading zeros in n. It's guaranteed that this situation is possible.


-----Output-----

Print the minimum number of digits in which the initial number and n can differ.


-----Examples-----
Input
3
11

Output
1

Input
3
99

Output
0



-----Note-----

In the first example, the initial number could be 12.

In the second example the sum of the digits of n is not less than k. The initial number could be equal to n.
"""

def min_digit_changes_to_meet_sum(k: int, n: str) -> int:
    # Calculate the initial sum of digits of n
    b_sum = sum(int(digit) for digit in n)
    
    # If the initial sum is already greater than or equal to k, no changes are needed
    if b_sum >= k:
        return 0
    
    # Convert the digits of n to a list of integers and sort them in ascending order
    lis = sorted(int(digit) for digit in n)
    
    # Initialize the count of changes needed
    c = 0
    
    # Iterate over the sorted list and try to increase the sum by changing the smallest digits first
    for digit in lis:
        # Increase the sum by the maximum possible value (9 - digit)
        b_sum += 9 - digit
        c += 1
        # Check if the sum is now greater than or equal to k
        if b_sum >= k:
            return c
    
    # If the loop completes without returning, it means we have changed all digits
    return c