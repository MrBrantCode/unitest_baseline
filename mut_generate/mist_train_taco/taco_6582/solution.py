"""
QUESTION:
You are given two four digit prime numbers Num1 and Num2. Find the distance of the shortest path from Num1 to Num2 that can be attained by altering only single digit at a time such that every number that we get after changing a digit is a four digit prime number with no leading zeros.
 
Example 1:
Input:
Num1 = 1033 
Num2 = 8179
Output: 6
Explanation:
1033 -> 1733 -> 3733 -> 3739 -> 3779 -> 8779 -> 8179.
There are only 6 steps reuired to reach Num2 from Num1. 
and all the intermediate numbers are 4 digit prime numbers.
 
Example 2:
Input:
Num1 = 1033 
Num2 = 1033
Output:
0
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes two integers Num1 and Num2 as input parameters and returns the distance of the shortest path from Num1 to Num2. If it is unreachable then return -1.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1000<=Num1,Num2<=9999
Num1 and Num2 are prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def shortest_path_between_primes(Num1, Num2):
    # Generate all four-digit prime numbers
    four_digit_primes = {num: 0 for num in range(1000, 10000) if is_prime(num)}
    
    from collections import deque
    queue = deque()
    queue.append([Num1, 0])
    four_digit_primes[Num1] = 1
    
    while queue:
        top = queue.popleft()
        num, step = str(top[0]), top[1]
        
        if int(num) == Num2:
            return step
        
        for place in range(4):
            temp = num[place]
            for digit in range(10):
                num = num[:place] + str(digit) + num[place + 1:]
                if int(num) in four_digit_primes and four_digit_primes[int(num)] == 0:
                    four_digit_primes[int(num)] = 1
                    queue.append([int(num), step + 1])
            num = num[:place] + str(temp) + num[place + 1:]
    
    return -1