"""
QUESTION:
Xenia the mathematician has a sequence consisting of n (n is divisible by 3) positive integers, each of them is at most 7. She wants to split the sequence into groups of three so that for each group of three a, b, c the following conditions held:  a < b < c;  a divides b, b divides c. 

Naturally, Xenia wants each element of the sequence to belong to exactly one group of three. Thus, if the required partition exists, then it has $\frac{n}{3}$ groups of three.

Help Xenia, find the required partition or else say that it doesn't exist.


-----Input-----

The first line contains integer n (3 ≤ n ≤ 99999) — the number of elements in the sequence. The next line contains n positive integers, each of them is at most 7.

It is guaranteed that n is divisible by 3.


-----Output-----

If the required partition exists, print $\frac{n}{3}$ groups of three. Print each group as values of the elements it contains. You should print values in increasing order. Separate the groups and integers in groups by whitespaces. If there are multiple solutions, you can print any of them.

If there is no solution, print -1.


-----Examples-----
Input
6
1 1 1 2 2 2

Output
-1

Input
6
2 2 1 1 4 6

Output
1 2 4
1 2 6
"""

def find_sequence_partition(n, sequence):
    # Count the occurrences of each number in the sequence
    count1 = sequence.count(1)
    count2 = sequence.count(2)
    count3 = sequence.count(3)
    count4 = sequence.count(4)
    count6 = sequence.count(6)
    
    # Check for invalid numbers in the sequence
    if 5 in sequence or 7 in sequence:
        return -1
    
    # Check if the counts allow for a valid partition
    if count2 < count4 or count2 - count4 != count6 - count3 or count1 != n / 3:
        return -1
    
    # Initialize the result list
    result = []
    
    # Form groups of (1, 2, 4)
    for _ in range(count4):
        result.append((1, 2, 4))
    
    # Form groups of (1, 3, 6)
    for _ in range(count3):
        result.append((1, 3, 6))
    
    # Form groups of (1, 2, 6)
    for _ in range(count2 - count4):
        result.append((1, 2, 6))
    
    return result