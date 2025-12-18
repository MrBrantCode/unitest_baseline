"""
QUESTION:
Write a function named `find_palindromic_numbers` that identifies and prints all palindromic numbers between 1 and a given number `n` (up to 1 billion), and returns the largest palindromic number within this range. Implement the solution without using any built-in functions or libraries to check for palindromic numbers, with a time complexity of O(n log n) and efficient memory usage.
"""

def find_palindromic_numbers(n):
    # Initialize the largest palindromic number as 0
    largest_palindrome = 0
    
    # Loop through numbers from 1 to n
    for num in range(1, n+1):
        # Convert the number to a string
        num_str = str(num)
        
        # Compare the string with its reverse
        if num_str == num_str[::-1]:
            # If the number is a palindrome, print it
            print(num)
            
            # Update the largest palindrome if necessary
            if num > largest_palindrome:
                largest_palindrome = num
    
    # Return the largest palindromic number
    return largest_palindrome