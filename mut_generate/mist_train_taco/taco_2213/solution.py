"""
QUESTION:
Miss DD is the most beautiful girl of NITJ.
While working on her final year project, Miss DD found some interesting numbers known as CooCoo Numbers.
The CooCoo numbers of order K are those numbers which have no. of prime divisors equal to K.
Miss DD is facing a problem while handling them. 
She wants to know  the count of all the CooCoo numbers of given order K which are less than or equal to N.

As she is not good in maths so she wants her boyfriend Divyank to solve this.

Input:

A number N will be given followed by Q the number of queries. 
Next Q lines will contain an integer K corresponding to the respective query.

Output:

Ouput the number of CooCoo numbers of order K which are less than or equal to N for each query.

Constraint:

2 ≤ N ≤ 1000000

1 ≤ K ≤ 10000000

1 ≤ Q ≤ 100000

SAMPLE INPUT
20
3
1
2
3

SAMPLE OUTPUT
12
7
0

Explanation

First Query : 

Order,k is 1 So the CooCoo numbers less than equal to 20 of order 1 are as follows 

2 3 4 5 7 8 9 11 13 16 17 19

Because each one of them have only one prime divisor.
"""

def count_coocoo_numbers(N, queries):
    # Initialize arrays to store the count of prime divisors and CooCoo numbers
    prime_divisors_count = [0] * (N + 1)
    coocoo_counts = [0] * (N + 1)
    
    # Calculate the number of prime divisors for each number up to N
    for i in range(2, N + 1):
        if prime_divisors_count[i] == 0:
            for j in range(i, N + 1, i):
                prime_divisors_count[j] += 1
    
    # Count the CooCoo numbers for each possible order
    for i in range(2, N + 1):
        coocoo_counts[prime_divisors_count[i]] += 1
    
    # Prepare the result for each query
    result = []
    for k in queries:
        if k <= N:
            result.append(coocoo_counts[k])
        else:
            result.append(0)
    
    return result