"""
QUESTION:
Given a string S of lowercase english characters, find out whether the summation of X and Y is even or odd, where X is the count of distinct characters which occupy even positions in english alphabets and have positive even frequency, and Y is the count of distinct characters which occupy odd positions in english alphabets and have positive odd frequency.
Note: Positive means greater than zero.
Example 1:
Input: S = "abbbcc"
Output: "ODD"
Explanation: X = 0 and Y = 1 so (X + Y) is 
ODD. 'a' occupies 1st place(odd) in english 
alphabets and its frequency is odd(1), 'b' 
occupies 2nd place(even) but its frequency 
is odd(3) so it doesn't get counted and 'c' 
occupies 3rd place(odd) but its frequency 
is even(2) so it also doesn't get counted.
Example 2:
Input: S = "nobitaa"
Output: "EVEN"
Explanation: X = 0 and Y = 2 so (X + Y) is
EVEN.
Your Task:  
You dont need to read input or print anything. Complete the function evenOdd() which takes S as input parameter and returns "EVEN"  if  X + Y is even, "ODD" otherwise.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1) 
Constraints:
1 ≤ |S| ≤ 1000
"""

def even_odd_sum(S: str) -> str:
    # Create a dictionary to map each character to its position in the alphabet
    alphabet_positions = {chr(i): i - 96 for i in range(97, 123)}
    
    # Create a dictionary to count the frequency of each character in the string
    frequency = {}
    for char in S:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Initialize counters for X and Y
    X = 0  # Count of distinct characters in even positions with positive even frequency
    Y = 0  # Count of distinct characters in odd positions with positive odd frequency
    
    # Calculate X and Y
    for char in frequency:
        position = alphabet_positions[char]
        freq = frequency[char]
        
        if position % 2 == 0:  # Even position in the alphabet
            if freq % 2 == 0:  # Positive even frequency
                X += 1
        else:  # Odd position in the alphabet
            if freq % 2 != 0:  # Positive odd frequency
                Y += 1
    
    # Determine if the sum of X and Y is even or odd
    if (X + Y) % 2 == 0:
        return "EVEN"
    else:
        return "ODD"