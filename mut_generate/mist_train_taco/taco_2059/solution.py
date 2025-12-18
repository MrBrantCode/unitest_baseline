"""
QUESTION:
Let S be the sum of divisors of an integer N excluding the number itself. When N = S, N is called a perfect number, when N> S, N is called a defendant number, and when N <S, N is called an abundant number. Create a program that determines whether a given integer is a perfect number, a missing number, or an abundant number.

Be careful not to exceed the program execution time.



Input

The input consists of a sequence of datasets. The number of datasets is 100 or less.

Each dataset consists of one row containing only the integer N (0 <N ≤ 100000000).

After the last dataset, there is a line marked 0 that marks the end of the input.

Output

For each dataset, print the string "` perfect number` "if the integer N is a perfect number," `deficient number`" if it is a missing number, or "` abundant number` "if it is an abundant number. ..

Example

Input

1
2
3
4
6
12
16
28
33550336
99999998
99999999
100000000
0


Output

deficient number
deficient number
deficient number
deficient number
perfect number
abundant number
deficient number
perfect number
perfect number
deficient number
deficient number
abundant number
"""

def classify_number(n):
    def sum_of_divisors(p):
        if p <= 1:
            return 0
        ans = 1
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                if i != p // i:
                    ans += i + p // i
                else:
                    ans += i
        return ans
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    s = sum_of_divisors(n)
    
    if n == s:
        return "perfect number"
    elif n > s:
        return "deficient number"
    else:
        return "abundant number"