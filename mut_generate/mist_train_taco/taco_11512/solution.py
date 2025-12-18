"""
QUESTION:
The number 105 is quite special - it is odd but still it has eight divisors.
Now, your task is this: how many odd numbers with exactly eight positive divisors are there between 1 and N (inclusive)?

-----Constraints-----
 - N is an integer between 1 and 200 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the count.

-----Sample Input-----
105

-----Sample Output-----
1

Among the numbers between 1 and 105, the only number that is odd and has exactly eight divisors is 105.
"""

def count_odd_numbers_with_eight_divisors(N: int) -> int:
    # List of known odd numbers with exactly eight divisors
    known_numbers = [105, 135, 165, 189, 195]
    
    # Initialize the count of such numbers
    count = 0
    
    # Iterate through the known numbers and count those that are <= N
    for number in known_numbers:
        if number <= N:
            count += 1
    
    return count