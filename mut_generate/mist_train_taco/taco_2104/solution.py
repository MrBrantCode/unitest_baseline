"""
QUESTION:
Ashley wrote a random number generator code.
Due to some reasons, the code only generates random positive integers which are not evenly divisible by 10. She gives $N$ and $S$ as input to the random number generator. The code generates a random number with number of digits equal to $N$ and sum of digits equal to $S$. The code returns -1 if no number can be generated. Print "-1" in such cases (without quotes). Else print the minimum possible product of digits of the random number generated.

-----Input:-----
- First line will contain a single integer $T$, the number of testcases. 
- Each testcase consists of two space separated integers, $N$ and $S$. 

-----Output:-----
For each testcase, output the answer on a new line.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 18$
- $1 \leq S \leq 5 * N$

-----Sample Input:-----
2
1 5

2 2

-----Sample Output:-----
5

1

-----EXPLANATION:-----
In first testcase, the only possible number of length 1 having digit sum 5 is 5. And it's product of digits is 5. 
In second testcase,  only possible two digit number as a generator output is 11(as 20 is divisible by 10, it is never generated) and product of it's digits is 1.
"""

def generate_min_product_of_digits(N, S):
    # Check if the sum of digits S can be achieved with N digits
    if S > 9 * N:
        return -1
    
    # Special case when N is 1
    if N == 1:
        return S
    
    # Initialize the product to 1 (since multiplying by 1 doesn't change the product)
    product = 1
    
    # Distribute the sum S among N digits to minimize the product
    for i in range(N):
        if S > 9:
            digit = 9
            S -= 9
        else:
            digit = S
            S = 0
        product *= digit
    
    # If there is any remaining sum, it means we couldn't distribute it properly
    if S > 0:
        return -1
    
    return product