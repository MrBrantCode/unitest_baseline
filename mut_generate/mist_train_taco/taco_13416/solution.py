"""
QUESTION:
Kuldeep's girlfriend Christie recently got her PhD in Maths. So to celebrate, they both decided to play games with mathematical sequences for their date nights.

The game they are playing today is "Jackpot Palindrome", the objective of the game is to find out length of the largest palindrome which only contains the digit "4" from a given string.

The reference string for today is the lucky string. Lucky string is the concatenation of all lucky numbers in ascending order.
 Lucky numbers are those numbers which contain only "4" and/or "5". For example 4, 5, 44, 54,55,444 are lucky numbers while 457, 987 ,154 are not.
So the fist few digits of the lucky string are "4544455455444445454455..." .

Since the lucky string is infinite, Christie gives Kuldeep an integer N and Kuldeep only needs to consider the lucky string upto length N.

Everytime Kuldeep answers correctly, he gets a kiss from Christie, obviously he'd want to maximize the number of kisses he gets, so your task is to help Kuldeep answer correctly everytime.

Input:
First line contains no of test cases T.
Next T lines contains a single integer N.

Output:
A single integer which is length of the largest palindrome substring containing only digit "4" in lucky string of length N.

Constraints:
1 ≤ T ≤ 100000
1 ≤ N ≤ 10^15

SAMPLE INPUT
4
1
2
3
4

SAMPLE OUTPUT
1
1
1
2
"""

def find_largest_palindrome_length(N):
    n = N
    length = 1
    
    while (n - 2 * length + 1) >= 0:
        n = n - (2 ** length) * length
        length += 1
    
    length -= 1
    
    m = 2 * length - 1
    
    if m > n:
        return m
    else:
        return n