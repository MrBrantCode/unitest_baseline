"""
QUESTION:
Let's solve the geometric problem

Mr. A is still solving geometric problems today. It is important to be aware of floating point errors when solving geometric problems.

Floating-point error is the error caused by the rounding that occurs when representing a number in binary finite decimal numbers. For example, 0.1 in decimal is an infinite decimal number of 0.00011001100110011 ... in binary, but an error occurs when rounding this to a finite number of digits.

Positive integers p and q are given in decimal notation. Find the b-ary system (b is an integer greater than or equal to 2) so that the rational number p / q can be expressed as a decimal number with a finite number of digits. If there are more than one, output the smallest one.

Constraints

* 0 <p <q <10 ^ 9



Input Format

Input is given from standard input in the following format.


p q


Output Format

Print the answer in one line.

Sample Input 1


1 2


Sample Output 1


2


1/2 is binary 0.1

Sample Input 2


21 30


Sample Output 2


Ten


21/30 is 0.7 in decimal





Example

Input

1 2


Output

2
"""

def find_smallest_base(p: int, q: int) -> int:
    def gcd(m: int, n: int) -> int:
        r = m % n
        return gcd(n, r) if r else n
    
    # Reduce the fraction by dividing both p and q by their greatest common divisor
    q //= gcd(p, q)
    
    # Find the smallest base b such that p/q can be expressed as a finite decimal number
    x = q
    y = 1
    k = 2
    
    while k * k <= x:
        if x % k == 0:
            while x % k == 0:
                x //= k
            y *= k
        k += 1
    
    y *= x
    return y