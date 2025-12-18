"""
QUESTION:
Kancha wants to participate in a new event of Technobyte. Event says that you have to write a number in seven segment display using matchsticks. Please refer to the diagram below for how many sticks are used for each digit !!

Now, event coordinator gave kancha a long string. your task is to tell how many matchsticks will be used in writing that number as in the seven segment display !!

Input:
First line of input contains an integer t, then t lines follow each containing a number less than 10^5 digits !

Output:
Print one line containing the integer denoting the number of matchsticks used.

Constraints:
0<t ≤10
0 ≤ Input number ≤ 10^(10^5)

SAMPLE INPUT
1
13579

SAMPLE OUTPUT
21

Explanation

1 takes 2 sticks
3 takes 5 sticks
5 takes 5 sticks
7 takes 3 sticks
9 takes 6 sticks
Total = 21 sticks
"""

def calculate_matchsticks(number_string: str) -> int:
    # List representing the number of matchsticks for each digit from 0 to 9
    matchsticks_per_digit = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    # Initialize the total matchsticks count
    total_matchsticks = 0
    
    # Iterate through each character in the number string
    for char in number_string:
        # Convert the character to an integer and get the corresponding matchsticks count
        digit = int(char)
        total_matchsticks += matchsticks_per_digit[digit]
    
    return total_matchsticks