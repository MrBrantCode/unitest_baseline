"""
QUESTION:
After a long vacation due to Swine Flu, 1st Year SVNIT students have returned back to Gajjar Bhavan. Students in Gajjar Bhavan generally handshake to greet each other but due to Swine Flu it's still risky to handshake so students greet each other by just words instead of handshakes.

Bagha is an interesting(really?) Maggu. He considers a greet interesting if the word spoken by a guy is palindrome and the length of the word is prime. Help, Bagha find out the number of interesting greets other students have given to him.

Input Format :
Input starts with N denoting the number of greets given to Bagha.
Next N lines contains a string(without space) each in lowercase having the greets.

Output Format :
Output the number of greets which are both palindromes and prime in length.

Constraints :
1 ≤ N ≤ 10
1 ≤ Length of string ≤ 1000

Problem Setter : Swastik Mundra

SAMPLE INPUT
3
hellolleh
naman
racecar

SAMPLE OUTPUT
2
"""

def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def is_palindrome(s):
    return s == s[::-1]

def count_interesting_greets(greets):
    count = 0
    for greet in greets:
        length = len(greet)
        if length > 1 and is_prime(length) and is_palindrome(greet):
            count += 1
    return count