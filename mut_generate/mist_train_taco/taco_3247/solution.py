"""
QUESTION:
As we have seen our little Vaishanavi playing with the plywood, her brother Vaishnav was playing
with numbers. 

Read about Factorial 

As we all know this kid always thinks in a different way than others think. He have some numbers with him. He wants to find out that if he finds the factorial of the numbers that he have how many times his lucky numbers are there in the factorial. Indeed this is simple.

Please help our little Vaishnav. Because you are ready to help him he will tell you that he has 2 lucky numbers
that are '4' & '7'. So if the number is 6 factorial is 720. So the count is 1. Suppose you got the
factorial as 447(JUST IMAGINE) your answer will be 3.

Input:

First line contains a single integer T, the number of test cases, followed by next T lines contains a single integer N.

Output:

Print the output for each query and separate each by an empty line.

Constraints:

1 ≤ T ≤ 100

1 ≤ N ≤ 250

Problem Setter : Bipin Baburaj

Problem Tester : Darshak Mehta

SAMPLE INPUT
3
1
6
8

SAMPLE OUTPUT
0
1
1
"""

def count_lucky_numbers_in_factorial(n, lucky_numbers=[4, 7]):
    def fact(n):
        if n < 2:
            return 1
        else:
            return n * fact(n-1)
    
    # Calculate the factorial of n
    factorial_value = fact(n)
    
    # Convert the factorial value to a string and then to a list of characters
    factorial_str = list(str(factorial_value))
    
    # Initialize the count of lucky numbers
    count = 0
    
    # Iterate through each character in the factorial string
    for char in factorial_str:
        if int(char) in lucky_numbers:
            count += 1
    
    return count