"""
QUESTION:
Little Panda has a thing for powers and modulus and he likes challenges. His friend Lucy, however, is impractical and challenges Panda to find both positive and negative powers of a number modulo a particular number. We all know that $A^{-1}\:{mod}\:X$ refers to the modular inverse of ${A}$ modulo ${X}$ (see Wikipedia).  

Since Lucy is impractical, she says that $A^{-n}\ \text{mod}\ X=(A^{-1}\ \text{mod}\ X)^n\ \text{mod}\ X$ for $n>0$.  

Now she wants Panda to compute $A^B\:{mod}\:X$.   

She also thinks that this problem can be very difficult if the constraints aren't given properly. Little Panda is very confused and leaves the problem to the worthy programmers of the world. Help him in finding the solution.

Input Format 

The first line contains ${T}$, the number of test cases. 

Then ${T}$ lines follow, each line containing ${A}$, ${B}$ and ${X}$.  

Output Format 

Output the value of $A^B\:{mod}\:X$.  

Constraints 

$1\leq T\leq1000$ 

$1\leq A\leq10^6$ 

$-10^6\leq B\leq10^6$ 

$1\leq X\leq10^6$ 

${A}$  and ${X}$ are coprime to each other (see Wikipedia)  

Sample Input  

3  
1 2 3  
3 4 2  
4 -1 5

Sample Output  

1  
1  
4  

Explanation 

Case 1: $1^2\ \text{mod}\ 3=1\ \text{mod}\ 3=1$ 

Case 2: $3^4\:\text{mod}\:2=81\:\text{mod}\:2=1$ 

Case 3: $4^{-1}\:\text{mod}\:5=4$
"""

def compute_power_mod(A: int, B: int, X: int) -> int:
    """
    Computes the value of A^B mod X.

    Parameters:
    A (int): The base number.
    B (int): The exponent.
    X (int): The modulus.

    Returns:
    int: The result of A^B mod X.
    """
    
    def extended_gcd(aa: int, bb: int) -> tuple:
        """
        Computes the extended greatest common divisor (gcd) of two numbers.

        Parameters:
        aa (int): The first number.
        bb (int): The second number.

        Returns:
        tuple: A tuple containing the gcd and the coefficients x and y such that ax + by = gcd(a, b).
        """
        (lastremainder, remainder) = (abs(aa), abs(bb))
        (x, lastx, y, lasty) = (0, 1, 1, 0)
        while remainder:
            (lastremainder, (quotient, remainder)) = (remainder, divmod(lastremainder, remainder))
            (x, lastx) = (lastx - quotient * x, x)
            (y, lasty) = (lasty - quotient * y, y)
        return (lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1))

    def modinv(a: int, m: int) -> int:
        """
        Computes the modular inverse of a modulo m.

        Parameters:
        a (int): The number to find the inverse of.
        m (int): The modulus.

        Returns:
        int: The modular inverse of a modulo m.
        """
        (g, x, y) = extended_gcd(a, m)
        if g != 1:
            raise ValueError("The modular inverse does not exist because the numbers are not coprime.")
        return x % m

    if B < 0:
        A = modinv(A, X)
        B = -B
    return pow(A, B, X)