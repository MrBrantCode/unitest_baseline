"""
QUESTION:
The Monk wants to teach all its disciples a lesson about patience, since they are always in a hurry to do something crazy. To teach them this, he gives them a list of N numbers, which may or may not be distinct. The students are supposed to solve a simple Mathematical equation based on the array of these N numbers.
g(x) - GCD (a[ 0 ], a[ 1 ], a[ 2 ]... a[n-1] )
f(x) - (a[ 0 ] * a[ 1 ] * a[ 2 ]... * a[n-1] )

The value of the MonkQuotient is: 10^9 + 7.

The equation to be solved is: ( f(x)^g(x) ) % MonkQuotient

Input constraints:
The first line of input will contain an integer — N. The next line will contain N integers denoting the elements of the list. 

Output constraints:
Print the required answer of the equation.

Constraints:
1 ≤ N ≤ 50 
1 ≤ Ai ≤ 10^3

SAMPLE INPUT
2
2 6

SAMPLE OUTPUT
144

Explanation

Here we can see that the product of the elements of array is 12 and the GCD of the array comes out to be 2 .
Thus the answer would be 12^2 which is 144.
"""

def calculate_monk_quotient(numbers):
    mod = 10**9 + 7
    
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    # Calculate g(x) - GCD of all elements in the list
    gx = numbers[0]
    for num in numbers[1:]:
        gx = gcd(gx, num)
    
    # Calculate f(x) - Product of all elements in the list
    fx = 1
    for num in numbers:
        fx = (fx * num) % mod
    
    # Calculate (f(x)^g(x)) % mod using exponentiation by squaring
    ans = 1
    while gx > 0:
        if gx & 1:
            ans = (ans * fx) % mod
        fx = (fx * fx) % mod
        gx //= 2
    
    return ans