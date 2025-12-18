"""
QUESTION:
Read problems statements in Mandarin Chinese here 

------ Problem Statement ------ 

Maxim likes dividers of the numbers. Also Maxim is fond of lucky numbers of small elephant from Lviv city.
 
If you remember, lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky, 5, 17, 467 — aren't.
 
Now Maxim is interested in the next information: what is the number of the integer positive dividers of number n, which are overlucky.
 
We call number overlucky if it is possible to remove some, but not all, digits and during bonding the remaining digits we will receive a lucky number. For example, number 72344 — overlucky, because it is possible to remove digits 2 and 3, and get number 744, which is lucky. Number 223 isn't overlucky. 

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. Single line of each test case contains an integer n. 

------ Output ------ 

For each test case on different lines print the answer to the problem.
------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ n ≤ 10^{9}$
 
----- Sample Input 1 ------ 
10
1
2
3
4
5
6
7
8
9
10
----- Sample Output 1 ------ 
0
0
0
1
0
0
1
1
0
0
"""

def count_overlucky_divisors(n: int) -> int:
    """
    Counts the number of overlucky divisors of a given number n.

    An overlucky number is a number that can be transformed into a lucky number
    by removing some, but not all, of its digits. A lucky number contains only
    the digits 4 and 7.

    Parameters:
    n (int): The number for which to count the overlucky divisors.

    Returns:
    int: The number of overlucky divisors of n.
    """
    overlucky_divisors = set()
    
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            s1 = str(j)
            s2 = str(n // j)
            if '4' in s1 or '7' in s1:
                overlucky_divisors.add(s1)
            if '4' in s2 or '7' in s2:
                overlucky_divisors.add(s2)
    
    return len(overlucky_divisors)