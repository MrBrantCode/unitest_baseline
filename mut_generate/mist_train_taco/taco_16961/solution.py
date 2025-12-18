"""
QUESTION:
Mani wants to eat chocolates, but her brother Pane does not give her the chocolates easily. Pane being a mathematician wants to teach Mani an important concept. Pane makes Mani stand on an infinite straight line. He marks all integers at equal divisions on the line and places chocolates on the integer X.

Initially Mani is on an integer Z. Mani can jump forward or backward from any general integer K. Pane being a mischievous brother puts a constraint that Mani can jump forward or backward only A, B or C integers i.e from any general integer K there are 6 possible moves (K+A, K-A, K+B, K-B, K+C, K-C). Pane gives Mani the liberty to choose distinct A, B and C in the range [1,100]. Find the probability that Mani succeeds in reaching the chocolates. Note that Mani is really clever and if she can reach the chocolates, she will.

Input :

First line contains an integer T containing test cases.
Each test case consists of a single line with two integers X and Z.

Output :

A single line for each test case having the answer rounded off to exactly 6 digits after the decimal.

Constraints :

1 ≤ T ≤ 10^5

1 ≤ X,Z ≤ 2 * 10^18

1 ≤ A,B,C ≤ 100

Author : Sayan

Tester : Shreyans

(By IIT Kgp HackerEarth Programming Club)

SAMPLE INPUT
3
2 10
15758 29586685
1000 1000000000

SAMPLE OUTPUT
0.956092
0.839450
0.999716
"""

def calculate_probability(X, Z, A, B, C):
    # Precomputed array based on the gcd values
    array = [814434, 99888, 28302, 12102, 5982, 2958, 1950, 1176, 924, 654, 474, 312, 204, 204, 114, 114, 60, 60, 60, 60, 24, 24, 24, 24, 24, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # Calculate the absolute difference between X and Z
    n = abs(X - Z)
    
    # Initialize the answer
    ans = 0
    
    # Sum the values in the array where n is divisible by the index + 1
    for j in range(1, 101):
        if n % j == 0:
            ans += array[j - 1]
    
    # Calculate the probability
    probability = ans / 970200.0
    
    # Return the probability rounded to 6 decimal places
    return round(probability, 6)