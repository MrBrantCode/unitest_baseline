"""
QUESTION:
You are given two four digit prime numbers Num1 and Num2. Find the distance of the shortest path from Num1 to Num2 that can be attained by altering only one single digit at a time. Every number obtained after changing a digit should be a four digit prime number with no leading zeros.
Example 1:
Input:
Num1 = 1033 
Num2 = 8179
Output: 6
Explanation:
1033 -> 1733 -> 3733 -> 3739 -> 3779
                 -> 8779 -> 8179.
There are only 6 steps required to reach
Num2 from Num1, and all the intermediate
numbers are 4 digit prime numbers.
Example 2:
Input:
Num1 = 1033 
Num2 = 1033
Output:
0
Your Task:  
You don't need to read input or print anything. Your task is to 
	Complete the constructor of the class Solution to precompute a list of prime numbers.  
	Complete function shortestPath() which takes two integers Num1 and Num2 as input parameters and returns the distance of the shortest path from Num1 to Num2. If it is unreachable then return -1.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1000  ≤ Num1,Num2  ≤ 9999
Num1 and Num2 are prime numbers.
"""

from collections import deque
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def convert_int_to_list(int_num):
    num_list = [0 for _ in range(4)]
    i = 3
    while i >= 0:
        num_list[i] = int_num % 10
        int_num //= 10
        i -= 1
    return num_list

def shortest_path_between_primes(Num1, Num2):
    if Num1 == Num2:
        return 0
    
    def bfs(start, target):
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            (num, steps) = queue.popleft()
            num_list = convert_int_to_list(num)
            if num == target:
                return steps
            for j in range(4):
                temp_num_list = list(num_list)
                for n in range(10):
                    if n != num_list[j]:
                        temp_num_list[j] = n
                        num_list_int = int(''.join((str(x) for x in temp_num_list)))
                        if num_list_int not in seen and is_prime(num_list_int) and (num_list_int >= 1000):
                            seen.add(num_list_int)
                            queue.append((num_list_int, steps + 1))
        return -1
    
    return bfs(Num1, Num2)