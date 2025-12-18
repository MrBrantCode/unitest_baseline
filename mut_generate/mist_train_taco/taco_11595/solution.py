"""
QUESTION:
Help Saurabh with his Chemistry Assignment.

Saurabh has been given a chemistry assignment by Ruby Mam. Though the assignment is simple but

Saurabh has to watch India vs Pakistan Match and he has no time to do the assignment by himself.

So Saurabh wants you to do his assignment so that he doesn’t get scolded by Ruby Mam . The assignment

is as follows , Suppose there are X particles initially at time t=0 in a box. At a time t the number of particles in

box becomes t times the number of particles at time t-1 . You will be given N and X where N is time at which the

number of particles in box is to be calculated and X is the number of particles at time t=0.

-----Input-----
The first line will contain the integer T, the number of test cases. Each test case consists of two space

separated integers N and X .

-----Output-----
For each test case, output the answer to the query. Since the output can be very large, output the answer modulo

10^6+3

-----Constraints-----
- 1 ≤ T ≤ 100000
- 1 ≤ N,X ≤ 10^18

-----Example-----
Input:
2
1 2
2 1

Output:
2
2

-----Explanation-----
Example case 2.At t=0 particles are 1 ,so at t=1 ,particles are 1*1 = 1 particles. At t=2, particles are 2*1 = 2 particles.
"""

def calculate_particles(N: int, X: int, M: int = 10**6 + 3) -> int:
    """
    Calculate the number of particles at time N given the initial number of particles X.

    Parameters:
    - N (int): The time at which the number of particles is to be calculated.
    - X (int): The number of particles at time t=0.
    - M (int): The modulo value (default is 10^6 + 3).

    Returns:
    - int: The number of particles at time N modulo M.
    """
    if N >= M:
        return 0
    else:
        # Precompute factorials modulo M up to M-1
        factorials = [1] * M
        for i in range(2, M):
            factorials[i] = factorials[i-1] * i % M
        
        # Return the result using the precomputed factorial
        return factorials[N] * X % M