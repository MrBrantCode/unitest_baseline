"""
QUESTION:
Given a number N, you need to write a program that finds the sum of digits of the number till the number becomes a single digit and then check whether the number is Prime/Non-Prime.
Example 1:
Input:
N=5602
Output:
0
Explanation:
1st step=5+6+0+2=13
2nd step=1+3=4
Since 4 is not prime, so answer is 0.
Example 2:
Input:
N=12
Output:
1
Explanation:
1st step=1+2=3
Since, 3 is prime, so answer =1.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function digitPrime() which takes a number N as input parameter and returns 1 if the final digit sum(adding digits until it becomes single-digit number) is prime.Otherwise, it returns 0.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

def digit_prime(N: int) -> int:
    # Convert the number to a string to process each digit
    m = str(N)
    
    # Reduce the number to a single digit by summing its digits
    while len(m) != 1:
        s = 0
        for i in m:
            s += int(i)
        m = str(s)
    
    # List of single-digit prime numbers
    list1 = [2, 3, 5, 7]
    
    # Check if the final single-digit number is in the list of primes
    if int(m) in list1:
        return 1
    return 0